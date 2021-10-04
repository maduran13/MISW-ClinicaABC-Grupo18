from flask_restful import Api
from flask_cors import CORS

from historiasClinicas import create_app
from historiasClinicas.vistas import VistaHistoriaClinica


app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
cors = CORS(app)

api.add_resource(VistaHistoriaClinica, '/historia-clinica')
