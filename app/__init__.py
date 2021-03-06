from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
mail = Mail()

photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    #creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.update(dict(
    SECRET_KEY="123456789",
    # WTF_CSRF_SECRET_KEY="a csrf secret key"
))

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
mail = Mail()

photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    #creating the app configurations
    app.debug=True;
    app.config.from_object(config_options[config_name])
    app.config.update(dict(
    SECRET_KEY="123456789",
    # WTF_CSRF_SECRET_KEY="a csrf secret key"
))

    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
