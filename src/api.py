import os
import sys
import subprocess
import ast
import connexion
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix
from flask_cors import CORS
import flask
import logging
import json
from datetime import datetime

from SPARQLWrapper import SPARQLWrapper, TURTLE, XML
from rdflib import Graph
# from kgx import RdfTransformer, PandasTransformer
# import zipfile

# from kgx_transformer import KgxTransformer
from reasonerapi_parser import reasonerapi_to_sparql, get_predicates_from_bio2rdf
from utils import get_data_dir


def start_api(port=8808, server_url='/', debug=False):
    """Start the Knowledge Collaboratory API using [zalando/connexion](https://github.com/zalando/connexion) and the `openapi.yml` definition

    :param port: Port of the API, defaults to 8808
    :param debug: Run in debug mode, defaults to False
    :param start_spark: Start a local Spark cluster, default to true
    """
    print("Starting the \033[1mTranslator Bio2RDF API\033[0m 🔮🐍")

    if debug:
        # Run in development mode
        deployment_server='flask'
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.DEBUG)
        print("Development deployment using \033[1mFlask\033[0m 🧪")
        print("Debug enabled 🐞 - The API will reload automatically at each change 🔃")
    else:
        # Run in productiom with tornado (also available: gevent)
        deployment_server='tornado'
        logging.basicConfig(level=logging.INFO)
        print("Production deployment using \033[1mTornado\033[0m 🌪️")
    

    api = connexion.App(__name__, options={"swagger_url": ""})
    # server_url = 'http://api.collaboratory.semantiscience.org'
    # api = connexion.App(__name__, options={"swagger_url": "", "disable_servers_overwrite": True}, arguments={'server_url': server_url})

    api.add_api('openapi.yml')
    # api.add_api('openapi.yml', arguments={'server_url': server_url}, validate_responses=True)

    # Add CORS support
    CORS(api.app)

    ## Fix to avoid empty list of servers for nginx-proxy deployments
    if os.getenv('LETSENCRYPT_HOST'):
        server_url='https://' + os.getenv('LETSENCRYPT_HOST')
        api.app.config['REVERSE_PROXY_PATH'] = server_url
        # api.app.config['REVERSE_PROXY_PATH'] = '/v1'
        ReverseProxyPrefixFix(api.app)
    elif os.getenv('VIRTUAL_HOST'):
        server_url='http://' + os.getenv('VIRTUAL_HOST')
        api.app.config['REVERSE_PROXY_PATH'] = server_url
        # api.app.config['REVERSE_PROXY_PATH'] = '/v1'
        ReverseProxyPrefixFix(api.app)

    print("Access Swagger UI at \033[1mhttp://localhost:" + str(port) + "\033[1m 🔗")
    api.run(host='0.0.0.0', port=port, debug=debug, server=deployment_server)


def get_predicates():
    """Get predicates and entities provided by the API
    
    :return: JSON with biolink entities
    """
    return get_predicates_from_bio2rdf()

def post_reasoner_query(request_body):
    """Get associations for a given ReasonerAPI query.
    
    :param request_body: The ReasonerStdAPI query in JSON
    :return: Results as a ReasonerStdAPI Message
    """
    query_graph = request_body["message"]["query_graph"]
    print(query_graph)
    if len(query_graph["edges"]) == 0:
        return ({"status": 400, "title": "Bad Request", "detail": "No edges", "type": "about:blank" }, 400)
    if len(query_graph["edges"]) > 1:
        return ({"status": 501, "title": "Not Implemented", "detail": "Multi-edges queries not yet implemented", "type": "about:blank" }, 501)

    reasonerapi_response = reasonerapi_to_sparql(request_body)
    # reasonerapi_response = request_body

    # TODO: populate edges/nodes with association predictions    
    #  Edge: {
    #     "id": "e50",
    #     "source_id": "MONDO:0021668",
    #     "target_id": "ChEMBL:CHEMBL560511",
    #     "type": "treated_by"
    #   }
    # Node: {
    #     "id": "ChEMBL:CHEMBL2106966",
    #     "name": "Piketoprofen",
    #     "type": "chemical_substance"
    #   },

    return reasonerapi_response or ('Not found', 404)

def get_kgx(from_kg):
    """Query the Bio2RDF SPARQL endpoint using CONSTRUCT queries 
    to retrieve BioLink nodes and edges (associations)
    Then convert the RDF to kgx TSV format
    And return the nodes/edges files in a zip file  
    """
    kgx_transformer = KgxTransformer(get_data_dir())
    resp = kgx_transformer.transform_rdf_to_kgx(from_kg)
    return resp

if __name__ == '__main__':

    debug = False
    if len(sys.argv) >= 2:
        if sys.argv[1]=='debug':
            debug = True

    server_url = "/"
    # Start API in debug mode 
    start_api(8808, server_url, debug)
