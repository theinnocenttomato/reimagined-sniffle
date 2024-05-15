from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField,SubmitField, SelectField
from wtforms.validators import DataRequired
from gamemoguls.models import Scenario, Locations

class ScenarioForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    statamount = IntegerField('Stat Amount', validators=[DataRequired()])
    death = BooleanField('Death', default=False)
    alignment = BooleanField('Alignment', default=False)
    winners = BooleanField('Winners', default=False)
    teams = BooleanField('Teams', default=False)
    multiseq = BooleanField('Multi-seq', default=False)
    locations = BooleanField('Locations', default=False)
    staff = BooleanField('Stats', default=False)
    staffstats = BooleanField('Staff Stats', default=False)
    staffamount = IntegerField('Staff Amount', validators=[DataRequired()])
    items = BooleanField('Items', default=False)

class PerformerCreationForm(FlaskForm):

        
        performername = StringField('Performer Name', validators=[DataRequired()])
        performerdescription = TextAreaField('Performer Description', validators=[DataRequired()])
        alignment = SelectField('Alignment', choices=[('1', 'Good'), ('0', "Netural" ), ("-1", "Bad")])
        # hometown = SelectField('Hometown', choices=[(location.id, location.name) for location in Locations.query.filter_by(type='city')])
        isactive = BooleanField('Is Active', default=False)
        isdead = BooleanField('Is Dead', default=False)


class LocationCreationForm(FlaskForm):
        
        locationname = StringField('Location Name', validators=[DataRequired()])
        locationtype = SelectField('Location Type', choices=[('city', 'City'), ('region', 'Region'), ('country', 'Country'), ('continent', 'Continent'), ('planet', 'Planet'), ('galaxy', 'Galaxy'), ('universe', 'Universe')],validators=[DataRequired()])
        locationdescription = TextAreaField('Location Description', validators=[DataRequired()])
        locationpopulation = IntegerField('Location Population', validators=[DataRequired()])


def ScenarioCreation(scenario):
    statamount = scenario.statamount


    class ScenarioCreationForm(FlaskForm):
        
        stat_fields = []
        staff_fields = []

        for i in range(statamount):
            stat_fields[f'stat_{i}'] = IntegerField(f'Stat {i}', validators=[DataRequired()])
        for i in range(scenario.staffamount):
            staff_fields[f'staff_{i}'] = IntegerField('Staff {i}', validators=[DataRequired()])

        

    return ScenarioCreationForm

def ItemCreation(scenario):

    class ItemCreationForm(FlaskForm):
        
        itemname = StringField('Item Name', validators=[DataRequired()])
        itemdescription = TextAreaField('Item Description', validators=[DataRequired()])
        itemtype = SelectField('Item Type', choices=[('weapon', 'Weapon'), ('armor', 'Armor'), ('consumable', 'Consumable'), ('misc', 'Misc')],validators=[DataRequired()])
        itemstats = IntegerField('Item Stats', validators=[DataRequired()])
    


    return ItemCreationForm


def StaffCreation(scenario):

    class StaffCreationForm(FlaskForm):
        
        staffname = StringField('Staff Name', validators=[DataRequired()])
        stafftype = SelectField('Staff Type', choices="test",validators=[DataRequired()])
    
    return StaffCreationForm

def storylinescreation(scenario):

    class StorylineCreationForm(FlaskForm):
        pass

    return StorylineCreationForm

def teamcreation(scenario):

    class TeamCreationForm(FlaskForm):
        pass

    return TeamCreationForm

