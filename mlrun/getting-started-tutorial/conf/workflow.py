
from kfp import dsl
from mlrun import mount_v3io

funcs = {}
DATASET = 'iris_dataset'
LABELS = "label"
MODELS = ["sklearn.ensemble.RandomForestClassifier",
          "sklearn.linear_model.LogisticRegression",
          "sklearn.ensemble.AdaBoostClassifier"]


# Configure function resources and local settings
def init_functions(functions: dict, project=None, secrets=None):
    for f in functions.values():
        f.apply(mount_v3io())

    functions['serving'].metadata.name = 'getting-started-serving'


# Create a Kubeflow Pipelines pipeline
@dsl.pipeline(
    name="Getting-started tutorial",
    description="This tutorial is designed to demonstrate some of the main "
                "capabilities of the Iguazio Data Science Platform.\n"
                "The tutorial uses the Iris flower data set."
)
def kfpipeline(source_url='http://iguazio-sample-data.s3.amazonaws.com/iris_dataset.csv'):

    # Ingest the data set
    ingest = funcs['get-data'].as_step(
        name="get-data",
        handler='get_data',
        inputs={'source_url': source_url},
        params={'format': 'pq'},
        outputs=[DATASET])

    # Analyze the dataset
    describe = funcs["describe"].as_step(
        name="summary",
        params={"label_column": LABELS},
        inputs={"table": ingest.outputs[DATASET]})

    # Train a model with hyperparemeters
    train = funcs["train"].as_step(
        name="train",
        params={"sample": -1,
                "label_column": LABELS,
                "test_size": 0.10},
        hyperparams={'model_pkg_class': MODELS},
        selector='max.accuracy',
        inputs={"dataset": ingest.outputs[DATASET]},
        outputs=['model', 'test_set'])

    # Test and visualize the model
    test = funcs["test"].as_step(
        name="test",
        params={"label_column": LABELS},
        inputs={"models_path": train.outputs['model'],
                "test_set": train.outputs['test_set']})

    # Deploy the model as a serverless function
    deploy = funcs["serving"].deploy_step(
        models={f"{DATASET}_v1": train.outputs['model']})

    # Test the new model server (via REST API calls)
    tester = funcs["serving-tester"].as_step(
        name='serving-tester',
        params={'addr': deploy.outputs['endpoint'], 'model': f"{DATASET}_v1"},
        inputs={'table': train.outputs['test_set']})
