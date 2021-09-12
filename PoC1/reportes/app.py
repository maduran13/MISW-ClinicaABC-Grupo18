from monitor.vistas.vistas import VistaHealthy
from flask_restful import Api
from monitor import create_app

app = create_app('default')
app_context = app.app_context()
app_context.push()


api = Api(app)
api.add_resource(VistaHealthy, '/health-check')
