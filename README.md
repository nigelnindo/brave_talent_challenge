# Brave Talent Python

Python Project for Brave Talent developer test.

## REST API Documentation

Copy [the](https://github.com/nigelnindo/brave_talent_python/blob/develop/swagger.yaml) contents of the Swagger YAML file into s Swagger Editor of your choice. If you don't have one, use the online editor found [here](https://editor2.swagger.io/). This it will then auto-generate the formatted documentation for you.

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

