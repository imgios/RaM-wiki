import os
from py2neo import Graph

def getConnection():
    dbUsername = 'neo4j'
    dbPassword = 'ramwiki'
    dbUrl = os.environ.get('ramwikiDBUrl', 'http://localhost:7474/db/data/')
    return Graph(dbUrl, auth = (dbUsername, dbPassword))