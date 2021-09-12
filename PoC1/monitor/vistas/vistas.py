from flask_restful import Resource
from flask import Response
import random

class VistaHealthy(Resource):
    def get(self):
        x = random.random()
        print("x = " + str(x))
        print("Return: " + "200" if (x > 0.4) else "500")
        if (x > 0.4):
            return Response("Ok", status=200, mimetype='application/json')
        else:
            return Response("Fail", status=500, mimetype='application/json')
