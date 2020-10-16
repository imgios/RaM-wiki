from flask import Blueprint, render_template, request
from .manager import EpisodeManager
from py2neo import Node

episodes = Blueprint (
    'episodes',
    __name__,
    template_folder='templates'
)

@episodes.route('/index')
@episodes.route('/')
def index():
    episodeManager = EpisodeManager()
    season = {}
    for i in range(1, 5): # [1, 5[
        result = episodeManager.getBySeason(i)
        season[str(i)] = len(result['data'])
    
    return render_template('episodes/index.html',
        season_episodes_number = season)

@episodes.route('/<string:episodeParam>')
def episodeInfo(episodeParam):
    """Character page that shows in-depth details."""
    episodeManager = EpisodeManager()
    result = episodeManager.getByEpisode(episodeParam)['data']
    if len(result) > 0:
        episode = result[0]['e'] # Episode found
        charactersInEpisode = episodeManager.getCharactersInEpisode(episode['no'])['data']
        if len(charactersInEpisode) > 0:
            episode['characters'] = charactersInEpisode
    else:
        episode = None # Episode not found
    
    return render_template('episodes/episodeInfo.html',
    episode = episode)

@episodes.route('/search')
def searchEpisode():
    """Episode search page that shows results based on the season given."""
    if 'season' in request.args:
        episodeManager = EpisodeManager()
        seasonNumber = request.args.get('season')
        data = episodeManager.getBySeason(seasonNumber)
        if len(data) > 0:
            episodes = [i for i in data['data']]
            results = []
            for episode in episodes:
                results.append({
                    'number': episode['e']['no'],
                    'episode': episode['e']['episode'],
                    'name': episode['e']['name'],
                    'air_date': episode['e']['air_date']
                })
        
        return render_template('episodes/search.html', results = results)