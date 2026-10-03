from flask import request, jsonify
from flask_restful import Resource
from src.service.MeteorologiaService import MeteorologiaService

class MeteorologiaList(Resource):
    def get(self):
        try:
            resultados = MeteorologiaService.listar_todas()
            return jsonify([r.__dict__ for r in resultados]), 200
        except Exception as e:
            return {"erro": str(e)}, 500

    def post(self):
        try:
            json_data = request.get_json()
            resultado = MeteorologiaService.criarMeteorologia(json_data)
            return jsonify(resultado.__dict__), 201
        except ValueError as e:
            return {"erro": str(e)}, 400

class MeteorologiaItem(Resource):
    def get(self, meteorologia_id):
        try:
            resultado = MeteorologiaService.buscar_por_id(meteorologia_id)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404

    def put(self, meteorologia_id):
        try:
            json_data = request.get_json()
            resultado = MeteorologiaService.atualizarMeteorologia(meteorologia_id, json_data)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404
        except ValueError as e:
            return {"erro": str(e)}, 400

    def delete(self, meteorologia_id):
        try:
            resultado = MeteorologiaService.deletarMeteorologia(meteorologia_id)
            return jsonify(resultado), 200
        except LookupError as e:
            return {"erro": str(e)}, 404