from flask import blueprints, render_template
from flask_login import current_user


main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main.html', current_user=current_user)