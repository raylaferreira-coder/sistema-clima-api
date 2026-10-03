from flask import request, jsonify
from flask_restful import Resource
from src.service.EnderecoService import EnderecoService

class EnderecoList(Resource):
    def get(self):
        try:
            resultados = EnderecoService.listar_todos()
            return jsonify([r.__dict__ for r in resultados]), 200
        except Exception as e:
            return {"erro": str(e)}, 500

    def post(self):
        try:
            json_data = request.get_json()
            resultado = EnderecoService.criarEndereco(json_data)
            return jsonify(resultado.__dict__), 201
        except ValueError as e:
            return {"erro": str(e)}, 400

class EnderecoItem(Resource):
    def get(self, endereco_id):
        try:
            resultado = EnderecoService.buscar_por_id(endereco_id)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404

    def put(self, endereco_id):
        try:
            json_data = request.get_json()
            resultado = EnderecoService.atualizarEndereco(endereco_id, json_data)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404
        except ValueError as e:
            return {"erro": str(e)}, 400

    def delete(self, endereco_id):
        try:
            resultado = EnderecoService.deletarEndereco(endereco_id)
            return jsonify(resultado), 200
        except LookupError as e:
            return {"erro": str(e)}, 404