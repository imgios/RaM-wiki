from ramwiki.utilities import getConnection, read_query_from_file
from py2neo import Graph

QUERY_PATH = 'ramwiki/characters/queries/'

class CharacterManager:
    def __init__(self):
        self.graph = getConnection()

    def getByName(self, characterName):
        query = read_query_from_file(QUERY_PATH + 'getCharacterByName.cyp')
        cursor = self.graph.run(query, character_name = characterName)
        return {"data": cursor.data()}

    def getByNumber(self, characterNumber):
        query = read_query_from_file(QUERY_PATH + 'getCharacterByNo.cyp')
        cursor = self.graph.run(query, character_number = characterNumber)
        return {"data": cursor.data()}

    def searchByName(self, characterName):
        query = read_query_from_file(QUERY_PATH + 'searchCharactersByName.cyp')
        cursor = self.graph.run(query, search_name = characterName)
        return {"data": cursor.data()}

    def getCharacterActingStats(self, characterNumber):
        query = read_query_from_file(QUERY_PATH + 'getCharacterActingStats.cyp')
        cursor = self.graph.run(query, character_number = characterNumber)
        return {"data": cursor.data()}

    #TO-DO: Add more function in order to retrive different data

