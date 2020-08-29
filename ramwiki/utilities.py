import os
import logging
from py2neo import Graph

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def getConnection():
    dbUsername = 'neo4j'
    dbPassword = 'ramwiki'
    dbUrl = os.environ.get('ramwikiDBUrl', 'http://localhost:7474/db/data/')
    return Graph(dbUrl, auth = (dbUsername, dbPassword))

def getNodesCount(dbGraph):
    try:
        nodesCount = len(dbGraph.nodes)
    except NameError:
        logger.warning("dbGraph not initialized: cannot retrieve nodes count.")
    else:
        return nodesCount

def getRelationshipsCount(dbGraph):
    try:
        relsCount = len(dbGraph.relationships)
    except NameError:
        logger.warning("dbGraph not initialized: cannot retrieve relationships count.")
    else:
        return relsCount

def read_query_from_file(cypher_file_path):
    with open(cypher_file_path, 'r') as cypher_file:
        cypher_query = cypher_file.read()
    return cypher_query

def getEntityCount(dbGraph, entity):
    # c = character, e = episode, l = location
    if entity == "c":
        query = read_query_from_file('cyphers/queries/getCharactersCount.cyp')
    elif entity == "e":
        query = read_query_from_file('cyphers/queries/getEpisodesCount.cyp')
    elif entity == "l":
        query = read_query_from_file('cyphers/queries/getLocationsCount.cyp')
    else:
        logger.warning("Entity not defined.")
    
    cursor = dbGraph.run(query)
    return cursor.data()[0]['count']
