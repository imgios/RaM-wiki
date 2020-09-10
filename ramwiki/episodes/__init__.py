from flask import Blueprint, render_template
from .manager import EpisodeManager

episodes = Blueprint (
    'episodes',
    __name__,
    template_folder='templates'
)

@episodes.route('/')
@episodes.route('/index')
def index():
    episodeManager = EpisodeManager()
    season = {}
    for i in range(1, 5): # [1, 5[
        result = episodeManager.getBySeason(i)
        season[str(i)] = len(result['data'])
    
    return render_template('episodes/index.html',
        season_episodes_number = season)