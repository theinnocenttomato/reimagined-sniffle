from flask import blueprints, render_template
from flask_login import current_user, login_required

play = blueprints.Blueprint('play', __name__)

@play.route('/play')
@login_required
def start_game():
    return render_template('play.html')