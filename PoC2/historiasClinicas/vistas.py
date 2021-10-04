from flask import jsonify
from flask_restful import Resource

class VistaHistoriaClinica(Resource):
    def get(self):
        return {
            "id": 123,
            "paciente": "Pedro Gonzales",
            "fecha_nacimiento": "15/09-1985",
            "historia": [
                {
                    "fecha": "29-08-2021",
                    "sintomas": "Dolor de estomago".
                    "diagnostico": "Gastroenteritis"
                }
            ]
        }
