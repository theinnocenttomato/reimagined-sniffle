from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import current_user, login_required
from gamemoguls.models import Scenario

edit = Blueprint('edit', __name__)


@edit.route('/edit/scenario', methods=['GET', 'POST'])
@login_required
def edit_scenario():
    scenarios = Scenario.query.filter_by(user_id=current_user.id)
    if request.method == 'POST':
        #User is logged in and submitting the form
        scenario_id = request.form.get('id')
        url = url_for('edit_scenario_details', scenario_id=str(scenario_id))
        return redirect(url)
    # Render the template
    return render_template('create/editscenario.html', scenarios=scenarios)

@edit.route('/edit/performer', methods=['GET', 'POST'])
@login_required
def edit_performer():
    return render_template('create/editperformer.html')

@edit.route('/edit/location', methods=['GET', 'POST'])
@login_required
def edit_location():
    return render_template('create/editlocation.html')

@edit.route('/edit/item', methods=['GET', 'POST'])
@login_required
def edit_item():
    return render_template('create/edititem.html')

@edit.route('/edit/staff', methods=['GET', 'POST'])
@login_required
def edit_staff():
    return render_template('create/editstaff.html')

@edit.route('/edit/company', methods=['GET', 'POST'])
@login_required
def edit_company():
    return render_template('create/editcompany.html')

@edit.route('/edit/team', methods=['GET', 'POST'])
@login_required
def edit_team():
    return render_template('create/editteam.html')
