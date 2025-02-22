from ramwiki.utilities import getConnection, read_query_from_file
from py2neo import Graph

QUERY_PATH = 'ramwiki/episodes/queries/'

class EpisodeManager:
    def __init__(self):
        self.graph = getConnection()
    
    def getBySeason(self, seasonNumber):
        query = read_query_from_file(QUERY_PATH + 'getBySeason.cyp')
        cursor = self.graph.run(query, season_number = seasonNumber)
        return {"data": cursor.data()}

    def getByEpisode(self, episode):
        query = read_query_from_file(QUERY_PATH + 'getByEpisode.cyp')
        cursor = self.graph.run(query, episode = episode)
        return {"data": cursor.data()}

    def getCharactersInEpisode(self, episodeNumber):
        query = read_query_from_file(QUERY_PATH + 'getCharactersInEpisode.cyp')
        cursor = self.graph.run(query, episode_number = episodeNumber)
        return {"data": cursor.data()}