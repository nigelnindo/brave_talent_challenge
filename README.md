# Brave Talent Python

Python Project for Brave Talent developer test.

## REST API 

The `host` and `port` for the Java API is `188.226.159.24:5000`

### API Documentation

Copy [the contents](https://github.com/nigelnindo/brave_talent_python/blob/develop/swagger.yaml) of the Swagger YAML file into a Swagger Editor of your choice. If you don't have one, use the online editor found [here](https://editor2.swagger.io/). This it will then auto-generate the formatted documentation for you.

### Examples

```shell
# Extract a number plate from a sentence 
$ curl -X GET "http://188.226.159.24:5000/api/extractor?sentence=Ken%20had%20a%20KCA%20001a%20yesterday." -H "accept: application/json"

# JSON result from API call
{
  "result": "KCA 001A"
}

# Get the Difference between two number plates
$ curl -X GET "http://188.226.159.24:5000/api/difference?firstPlate=KAZ%20999Z&secondPlate=KBA%20001A" -H "accept: application/json"

# JSON result from API call
{
  "result": 1
}

```

## Docker

This project can be run as a Docker container.

### Run with Docker

[Install](https://docs.docker.com/engine/installation/) Docker for you Operating System. Beyond the scope of this document.

```shell
# Pull latest image from the public repository
$ docker pull nigelnindo/brave-talent-python

# Run the image and bind ports
docker run -d -p 5000:5000 nigelnindo/brave-talent-python
```

Visit localhost:5000 on your browser.

## Run locally

Requires Python 2.7 & `pip` installed. Clone project then run:

```shell
# get project dependencies
$ pip install -r requirements.txt

# start server
$ python source/Server.py
```

## Deployment

[Deployment 1](https://github.com/nigelnindo/brave_talent_java/blob/develop/deployment_1.png) outlines the build process from local to DockerHub, and [Deployment 2](https://github.com/nigelnindo/brave_talent_java/blob/develop/deplyoment_2.png) outlines the build process from DockerHub to the a client connection.
