from gateway import create_app
from flask_restful import Resource, Api
from flask import request
import requests

app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaSignIn(Resource):
    def post(self):
        url = 'http://127.0.0.1:5001/signin'
        name=request.json["name"]
        password=request.json["password"]
        role=request.json["role"]
        myobj = {'name': name,'password': password,'role': role}
        response = requests.post(url, json = myobj)
        return response.json()

class VistaLogIn(Resource):
    def post(self):
        name=request.json["name"]
        password=request.json["password"]
        role=request.json["role"]
        url = 'http://127.0.0.1:5001/auth/userrole'
        myobj = {'name': name,'password': password,'role': role}
        response = requests.post(url, json = myobj)
        return response.json()

class VistaHistoriaClinica(Resource): 
    def get(self):
        token = request.json["token"]
        url = 'http://127.0.0.1:5001/validate-token'
        myobj = {'token': token}
        response = requests.post(url, json = myobj)
        if response.status_code != 200 :
            return response.text

        #llamar api de historia clinica
        response = requests.get('http://127.0.0.1:5002/historia-clinica')
        return response.json()

api.add_resource(VistaSignIn, '/signIn')
api.add_resource(VistaLogIn, '/logIn')
api.add_resource(VistaHistoriaClinica, '/historia-clinica') 