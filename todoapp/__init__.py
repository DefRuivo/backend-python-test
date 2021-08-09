from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from todoapp.models.model import configure as config_db



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "uwa"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
    
    from todoapp.views import bp
    app.register_blueprint(bp)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.blueprint_login_view = "bp.index"

    from todoapp.models.model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    Bootstrap(app)
    config_db(app)
    Migrate(app, app.db)
    return app