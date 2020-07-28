# Data Science from Research to Production with Jupyter, Kubeflow & Nuclio
## MLConference (29.07.2020)

A workshop, showing how to use [**Nuclio**](http://nuclio.io) & [**MLRun**](http://www.github.com/mlrun/mlrun) with [*Kubeflow*](https://www.kubeflow.org/) to deploy end to end machine learning pipelines, with Multiple runtimes (serverless functions, jobs, etc...), Artifacts & Code tracking and Automation directly from your jupyter notebook!

## Preperations
### Install Nuclio [[website](http://nuclio.io)|[github](http://www.github.com/nuclio/nuclio)]
 - Locally on docker: ```docker run -p 8070:8070 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp nuclio/dashboard:stable-amd64```
 - On Kubernetes (Or local minikube) / AKS / GCP: [Nuclio installation notes](https://nuclio.io/docs/latest/setup/)

### Jupyter integration
- ```pip install nuclio-jupyter```
 
### Install MLRun [[github](https://github.com/mlrun/mlrun)]
- ```pip install mlrun```
- Install API and UI endpoints locally [with this guide](https://github.com/mlrun/mlrun/tree/development/hack/local)

## What will we do?
1. Review some background about the problems of moving to production and how we can use this set of tools to help automate it.
2. We will review how Nuclio integrates with Jupyter for easy deployment by using `nuclio-jupyter`.  
We will deploy an [example translation (NLP) endpoint](nuclio/nlp-example.ipynb) and use this template to create a function of our own.
3. We will review MLRun with some [basics](mlrun/basics), a full [getting started](mlrun/getting-started-tutorial/getting-started-tutorial.ipynb) tutorial to setup a project, tracking results, lunching a pipeline and an [example project](mlrun/sklearn-pipe/sklearn-project.ipynb)

Through this process we will share about best practices, how to ease our work and innovate fast!

