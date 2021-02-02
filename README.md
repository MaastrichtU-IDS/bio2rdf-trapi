[![TRAPI version](https://img.shields.io/badge/TRAPI-v1.0.0-blueviolet)](https://github.com/NCATSTranslator/ReasonerAPI)

Query Bio2RDF using the [Translator Reasoner API](https://github.com/NCATSTranslator/ReasonerAPI) (TRAPI)

**[🔗 https://api.bio2rdf.137.120.31.102.nip.io](https://api.bio2rdf.137.120.31.102.nip.io)**

## Deploy Bio2RDF TRAPI 🛩️

Starts the Translator Reasoner API to query the Bio2RDF SPARQL endpoint

* The TRAPI-SPARQL interface is implemented in Python in the `src/` folder
* Uses OpenAPI 3 with Swagger UI, built in Python using [zalando/connexion](https://github.com/zalando/connexion)

> Requires [Python 3.7+](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)

1. Clone the repository

```bash
git clone https://github.com/MaastrichtU-IDS/bio2rdf-trapi.git
cd bio2rdf-trapi
```

2. Install dependencies

```bash
pip3 install -r requirements.txt
```

> If you are facing conflict with already installed packages, then you might want to use a [Virtual Environment](https://docs.python.org/3/tutorial/venv.html) to isolate the installation in the current folder before installing bio2rdf-trapi:
>
> ```bash
> # Create the virtual environment folder in your workspace
> python3 -m venv .venv
> # Activate it using a script in the created folder
> source .venv/bin/activate
> ```
>

3. Start the API in **production** mode on http://localhost:8808 with Tornado:

```bash
python3 src/api.py
```

Or start the API in **debug** mode with Flask (the API will be reloaded automatically at each change to the code):

```bash
python3 src/api.py debug
```

>  Check [CONTRIBUTING.md](/CONTRIBUTING.md) for more details on how to run the API locally and contribute.

### Start with Docker 🐳

Requirements: [Docker](https://docs.docker.com/get-docker/).

Build and start the container with [docker-compose](https://docs.docker.com/compose/) on [http://localhost:8808](http://localhost:8808)

```bash
docker-compose up -d --build
```

> We use [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy) and [docker-letsencrypt-nginx-proxy-companion](https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion) as reverse proxy for HTTP and HTTPS in production. You can change the proxy URL and port via environment variables `VIRTUAL_HOST`, `VIRTUAL_PORT` and `LETSENCRYPT_HOST` in the [docker-compose.yml](https://github.com/MaastrichtU-IDS/bio2rdf-trapi/blob/master/docker-compose.yml) file.

Check the logs:

```bash
docker-compose logs
```

Stop the container:

```bash
docker-compose down
```

## Overview of API operations 🧭

Overview of the different operations available in Bio2RDF Translator Reasoner API (supporting `kgx`)

### Query operation

The user sends a [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) query to Bio2RDF Nanopublications in the BioLink format (e.g. drug indications). The query is a graph with nodes and edges defined in JSON, and uses classes from the [BioLink model](https://biolink.github.io/biolink-model).

### Predicates operation

The `/predicates` operation will return the entities and relations provided by this API in a JSON object (following the [ReasonerAPI](https://github.com/NCATSTranslator/ReasonerAPI) specifications).

# Acknowledgments

Service funded by the [NIH NCATS Translator project](https://ncats.nih.gov/translator/about). 

![Funded the the NIH NCATS Translator project](https://ncats.nih.gov/files/TranslatorGraphic2020_1100x420.jpg)