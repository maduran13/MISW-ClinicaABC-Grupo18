from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY']='experimento-seguridad-ii'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'users', #Nombre DB de MongoDB
        'host': 'localhost', #Host de MongoDB
        'port': 5000 #Puerto de MongoDB
    }
    return app