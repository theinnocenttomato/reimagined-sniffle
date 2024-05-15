from flask import blueprints, render_template, redirect, url_for, flash, request
from gamemoguls.models import Scenario, Users
from gamemoguls import db


view = blueprints.Blueprint('view', __name__)


@view.route('/scenario', methods=['GET', 'POST'])
def view_scenarios():
    scenarios = db.session.query(Scenario, Users.username).join(Users).all()
    if request.method == 'POST':
        scenario_id = request.form.get('id')
        url = url_for('viewscenarios', scenario_id=str(scenario_id))
        return redirect(url)
    return render_template('view/viewscenarios.html', scenarios=scenarios)

@view.route('/scenario/<int:scenario_id>', methods=['GET', 'POST'])
def view_scenario_details(scenario_id):
    scenario = Scenario.query.get_or_404(scenario_id)
    author = db.session.query(Users).join(Scenario).filter(Scenario.id == scenario_id).all()
    return render_template('view/view_scenario_details.html', scenario=scenario, author=author)

@view.route('/view/performer', methods=['GET', 'POST'])
def view_performers():
    return render_template('view/viewperformer.html')

@view.route('/view/location', methods=['GET', 'POST'])
def view_locations():
    return render_template('view/viewlocation.html')

@view.route('/view/item', methods=['GET', 'POST'])
def view_items():
    return render_template('view/viewitem.html')

@view.route('/view/staff', methods=['GET', 'POST'])
def view_staff():
    return render_template('view/viewstaff.html')

@view.route('/view/company', methods=['GET', 'POST'])
def view_company():
    return render_template('view/viewcompany.html')

@view.route('/view/team', methods=['GET', 'POST'])
def view_teams():
    return render_template('view/viewteam.html')