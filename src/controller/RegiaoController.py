from flask import request, jsonify
from flask_restful import Resource
from src.service.RegiaoService import RegiaoService

class RegiaoList(Resource):
    def get(self):
        try:
            resultados = RegiaoService.listar_todas()
            return jsonify([r.__dict__ for r in resultados]), 200
        except Exception as e:
            return {"erro": str(e)}, 500

    def post(self):
        try:
            json_data = request.get_json()
            resultado = RegiaoService.criarRegiao(json_data)
            return jsonify(resultado.__dict__), 201
        except ValueError as e:
            return {"erro": str(e)}, 400

class RegiaoItem(Resource):
    def get(self, regiao_id):
        try:
            resultado = RegiaoService.buscar_por_id(regiao_id)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404

    def put(self, regiao_id):
        try:
            json_data = request.get_json()
            resultado = RegiaoService.atualizarRegiao(regiao_id, json_data)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404
        except ValueError as e:
            return {"erro": str(e)}, 400

    def delete(self, regiao_id):
        try:
            resultado = RegiaoService.deletarRegiao(regiao_id)
            return jsonify(resultado), 200
        except LookupError as e:
            return {"erro": str(e)}, 404