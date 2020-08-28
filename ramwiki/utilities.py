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
        logger.warning("dbGrapg not initialized: cannot retrieve nodes count.")
    else:
        return nodesCount

def getRelationshipsCount(dbGraph):
    try:
        relsCount = len(dbGraph.relationships)
    except NameError:
        logger.warning("dbGraph not initialized: cannot retrieve nodes count.")