from flask import Flask

def create_app():
    app = Flask(__name__)
    app.run(port=5001)

    return app