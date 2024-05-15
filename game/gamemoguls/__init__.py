from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from gamemoguls.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
mail=Mail()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    app.jinja_env.globals['getattr'] = getattr
    print(app.config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from gamemoguls.models import Users, Scenario, Scenariorating, Translations, Locations, Staff, logs, Companies
    with app.app_context():
        db.create_all()

    from gamemoguls.main.routes import main
    from gamemoguls.users.routes import users
    from gamemoguls.play.routes import play
    from gamemoguls.view.routes import view
    from gamemoguls.create.routes import create
    from gamemoguls.edit.routes import edit
    from gamemoguls.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(play)
    app.register_blueprint(view)
    app.register_blueprint(create)
    app.register_blueprint(edit)
    app.register_blueprint(errors)

    return app