# Data Science from Research to Production with Jupyter, Kubeflow & Nuclio
## MLConference (16.11.2020)

A workshop, showing how to use [**Nuclio**](http://nuclio.io) & [**MLRun**](http://www.github.com/mlrun/mlrun) with [*Kubeflow*](https://www.kubeflow.org/) to deploy end to end machine learning pipelines, with Multiple runtimes (serverless functions, jobs, etc...), Artifacts & Code tracking and Automation directly from your jupyter notebook!

## Preperations

We will install Nuclio and MLRun (Jupyter environment and UI) over docker for easy installation.
- Nuclio [[website](http://nuclio.io)|[github](http://www.github.com/nuclio/nuclio)|[installation notes](https://nuclio.io/docs/latest/setup/)]
- MLRun [[github](https://github.com/mlrun/mlrun)|[installation notes](https://github.com/mlrun/mlrun/tree/development/hack/local)]
### Pull images

```
docker pull quay.io/nuclio/dashboard:stable-amd64
docker pull mlrun/jupyter:TMLS
docker pull mlrun/mlrun-ui:0.5.4
```

### Run containers

You can change the `SHARED_DIR` to another path for storing the data/artifacts

```
SHARED_DIR=~/mlrun-data
docker network create mlrun-network
docker run -it -p 8080:8080 -p 8888:8888 --rm -d --network mlrun-network --name jupyter -e NUCLIO_DASHBOARD_URL=http://nuclio:8070  -v ${SHARED_DIR}:/home/jovyan/data mlrun/jupyter:TMLS
docker run -it -p 4000:80 --rm -d --network mlrun-network --name mlrun-ui -e MLRUN_API_PROXY_URL=http://jupyter:8080 mlrun/mlrun-ui:0.5.4
docker run -p 8070:8070 --rm -d --network mlrun-network --name nuclio -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp quay.io/nuclio/dashboard:stable-amd64
```

Open the browser pointing to Jupyter, Nuclio, and MLRUn UIs at:
* Jupyter: http://localhost:8888/
* MLRun: http://localhost:4000/
* Nuclio: http://localhost:8070/



## What will we do?
1. Review some background about the problems of moving to production and how we can use this set of tools to help automate it.
2. We will review how Nuclio integrates with Jupyter for easy deployment by using `nuclio-jupyter`.  
We will deploy an [example translation (NLP) endpoint](nuclio/nlp.ipynb) and use this template to create a function of our own.
3. We will review MLRun with some [basics](mlrun/basics) and a [local example](mlrun/local-sklearn-pipe/skpipe.ipynb), a full [getting started](mlrun/getting-started-tutorial/getting-started-tutorial.ipynb) tutorial to setup a project, tracking results, lunching a pipeline and how to easily create serving endpoints with [MLRun's Serving runtime](mlrun/model_serving/v2_model_server.ipynb).

Through this process we will share about best practices, how to ease our work and innovate fast!

