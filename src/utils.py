import os

def get_data_dir(file=''):
    """Return the full path to the directory used to store the API data
    """
    data_dir = os.getenv('TRAPI_DATA_DIR')
    if not data_dir:
        # Output data folder in current dir if not provided via environment variable
        data_dir = os.getcwd() + '/output/'
    else:
        if not data_dir.endswith('/'):
            data_dir += '/'
    return data_dir + file

def get_sparql_endpoint_url():
    """Return the SPARQL endpoint used by the API"""
    sparql_endpoint = os.getenv('TRAPI_SPARQL_ENDPOINT')
    if not sparql_endpoint:
        sparql_endpoint = 'https://bio2rdf.137.120.31.102.nip.io/sparql'
    return sparql_endpoint