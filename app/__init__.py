from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options

bootstrap = Bootstrap() 

def create_app(config_name):

    # creating the app instance
    app = Flask(__name__)

    # creating app configuration 
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
     
    # initialaizing the app extentions 
    bootstrap.init_app(app)
    
    #register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # setting the configuration 
    from requests import config_requests
    config_requests(app)

    return app


