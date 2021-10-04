from flask_jwt_extended.jwt_manager import JWTManager
from authorizing import create_app
from flask_restful import Resource, Api
from flask import request
from .modelos import db, User
from flask_jwt_extended import create_access_token

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)

api = Api(app)
        
class VistaUser(Resource):
    def post(self):
        new_user = User(name=request.json["name"], password=request.json["password"], role=request.json["role"])
        new_user.save()
        token_de_acceso = create_access_token(identity=new_user.name)
        return {"mensaje":"usuario creado exitosamente", "token":token_de_acceso}

class VistaGenerateToken(Resource):

    def post(self):
        name=request.json["name"]
        password=request.json["password"]
        role=request.json["role"]
        user = User.objects(name=name,password=password,role=role).first()
        if not user:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=user.name)
            return {"mensaje":"Token generado exitosamente", "token": token_de_acceso}

api.add_resource(VistaUser, '/signin')
api.add_resource(VistaGenerateToken, '/auth/userrole')

jwt = JWTManager(app)