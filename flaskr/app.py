from flaskr.notifier import VistaNotifier
from flaskr import create_app
from flask_restful import Api
from flask_cors import CORS

app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
cors = CORS(app)

api.add_resource(VistaNotifier, '/notify')
