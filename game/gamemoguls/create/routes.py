from flask import blueprints, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from gamemoguls.create.forms import ScenarioForm, ScenarioCreation, LocationCreationForm, PerformerCreationForm
from gamemoguls.models import Scenario, Locations, Performers, logs
from gamemoguls import db

import sqlite3


create = blueprints.Blueprint('create', __name__)

@create.route('/create/scenario', methods=['GET', 'POST'])
@login_required
def create_scenario():
    form = ScenarioForm()
    if form.validate_on_submit():
        scenario = Scenario(name=form.name.data,
                            description=form.description.data,
                            statamount=form.statamount.data,
                            death=form.death.data,
                            alignment=form.alignment.data,
                            winners=form.winners.data,
                            teams=form.teams.data,
                            multiseq=form.multiseq.data,
                            locations=form.locations.data,
                            staff=form.staff.data,
                            staffstats=form.staffstats.data,
                            staffamount=form.staffamount.data,
                            items=form.items.data,
                            user_id=current_user.id)
        
        try:
            db.session.add(scenario)
            db.session.commit()
            scenario = Scenario.queryfilter_by(scenario_id=scenario.id)
            db_name = f'scenario_{scenario.id}'
            db_path = f'./defaultscenarios/{db_name}.db'  # Note the use of the "./" prefix to make it a relative path
            conn = sqlite3.connect(db_path)
            # creates the scenario table
            conn.execute("CREATE TABLE IF NOT EXISTS scenario (id INTEGER PRIMARY KEY, name TEXT, description TEXT, statamount INTEGER, death BOOLEAN, alignment BOOLEAN, winners BOOLEAN, teams BOOLEAN, multiseq BOOLEAN, locations TEXT, staff TEXT, staffstats TEXT, staffamount INTEGER, items TEXT)")
            # copys the data from the master database to the scenario database
            conn.execute("INSERT INTO scenario (id,name, description, statamount, death, alignment, winners, teams, multiseq) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (scenario.id, scenario.name, scenario.description, scenario.statamount, scenario.death, scenario.alignment, scenario.winners, scenario.teams, scenario.multiseq, scenario.locations, scenario.staff, scenario.staffstats, scenario.staffamount, scenario.items))
            conn.commit()
            conn.close()
            flash('Scenario created successfully!')
            return redirect(url_for('edit_scenario_details', scenario_id=scenario.id))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating the scenario. Please try again.')
            print(str(e))

    return render_template('create/createscenario.html', form=form)

@create.route('/create/scenario/<int:scenario_id>', methods=['GET', 'POST'])
@login_required
def create_scenario_details(scenario_id):
    scenario = Scenario.query.get_or_404(scenario_id)
    if current_user.id == scenario.user_id:

        form = ScenarioCreation(scenario_id=scenario_id)


        num_stats = scenario.statamount
        stat_fields = []
        for i in range(num_stats):
            field_name = f'stat_{i+1}'
            stat_fields.append((field_name, 'text'))

        fields = [
            *stat_fields,
            ('death', 'checkbox'),
            ('alignment', 'checkbox'),
            ('winners', 'checkbox'),
            ('teams', 'checkbox'),
            ('multiseq', 'checkbox')
        ]

        if request.method == 'POST':
            scenario = Scenario.query.get_or_404(scenario_id)

            # checks the name of the columns in the database

            i = scenario.statamount
            db_name = f'scenario_{scenario.id}'
            db_path = f'./instance/defaultscenarios/{db_name}.db'


@create.route('/create/scenario/<int:scenario_id>', methods=['GET', 'POST'])
@login_required
def edit_scenario_details(scenario_id):
    scenario = Scenario.query.get_or_404(scenario_id)
    if current_user.id == scenario.user_id:

        form = ScenarioCreation(scenario_id=scenario_id)


        num_stats = scenario.statamount
        stat_fields = []
        for i in range(num_stats):
            field_name = f'stat_{i+1}'
            stat_fields.append((field_name, 'text'))

        fields = [
            *stat_fields,
            ('death', 'checkbox'),
            ('alignment', 'checkbox'),
            ('winners', 'checkbox'),
            ('teams', 'checkbox'),
            ('multiseq', 'checkbox')
        ]

        if request.method == 'POST':
            scenario = Scenario.query.get_or_404(scenario_id)

            # checks the name of the columns in the database

            i = scenario.statamount
            db_name = f'scenario_{scenario.id}'
            db_path = f'./instance/defaultscenarios/{db_name}.db'  # Note the use of the "./" prefix to make it a relative path
            conn = sqlite3.connect(db_path)

            for i in range(i):
                try:
                    conn.execute("ALTER TABLE scenario ADD COLUMN stat_{} TEXT".format(i+1))
                except sqlite3.OperationalError:
                    pass
            query = f"INSERT INTO scenario (name, description, statamount, death, alignment, winners, teams, multiseq"
            values = (scenario.name, scenario.description, scenario.statamount, scenario.death, scenario.alignment, scenario.winners, scenario.teams, scenario.multiseq)

            statarry = []

            i = scenario.statamount

            for i in range(i):
                stats = request.form.get(f'stat_{i+1}')
                statarry.append(f'{stats}')

            statstring = tuple(statarry)

            i = scenario.statamount

            for i in range(i):
                query += f", stat_{i+1}"

            values += (statstring,)
            query += ") VALUES ("
            query += ", ".join(["?"] * (len(values) + 1))
            query += ")"

            conn.execute(query, values)

            conn.commit()
            conn.close()

            action= logs(logcreatorid=current_user.id,logtype='createscenario',logtext=f'User {current_user.username}',logorigin='createscenario')
            db.session.add(action)
            db.session.commit()
            return render_template('create/edit_scenario_details.html', scenario=scenario, fields=fields)

    else:
        flash('You do not have permission to edit this scenario.')
        action = logs(logcreatorid=current_user.id,logtype='permissiondenied',logtext=f'User {current_user.username} tried to edit scenario {scenario.name} but did not have permission to do so.',logorigin='createscenario')
        db.session.add(action)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('create/edit_scenario_details.html', scenario=scenario, fields=fields)

@create.route('/create/performer', methods=['GET', 'POST'])
@login_required
def create_performer():
    form = PerformerCreationForm()
    if form.validate_on_submit():
        performer = Performers(name=form.name.data,
                               age=form.age.data,
                               pronouns=form.pronouns.data,
                               hometown=form.hometown.data,
                               alignment=form.alignment.data,
                               isactive=form.isactive.data,
                               death=form.death.data)
        try:
            db.session.add(performer)
            db.session.commit()
            flash('Performer created successfully!')
            action = logs(logcreatorid=current_user.id, logtype='creation', logtext=f'Created performer {performer.name}',logorigin='createperfomer')
            db.session.add(action)
            db.session.commit()
            return redirect(url_for('create.createperformer'))
        except Exception as e:
            db.session.rollback()
            action = logs(logcreatorid=current_user.id, logtype='creationfailure', logtext=(str(e)),logorigin='createperfomer')
            db.session.add(action)
            db.session.commit()
            flash('An error occurred while creating the performer. Please try again.')



    return render_template('create/createperformer.html')

@create.route('/create/location', methods=['GET', 'POST'])
@login_required
def create_location():
    return render_template('create/createlocation.html')

@create.route('/create/item', methods=['GET', 'POST'])
@login_required
def create_item():
    return render_template('create/createitem.html')

@create.route('/create/company', methods=['GET', 'POST'])
@login_required
def create_company():
    return render_template('create/createcompany.html')

@create.route('/create/staff', methods=['GET', 'POST'])
@login_required
def create_staff():
    return render_template('create/createstaff.html')

@create.route('/create/team', methods=['GET', 'POST'])
@login_required
def create_team():
    return render_template('create/createteam.html')