from flask import request, jsonify
from flask_restful import Resource
from src.service.UsuarioService import UsuarioService

class UsuarioList(Resource):
    def get(self):
        try:
            resultados = UsuarioService.listar_todos() 
            return jsonify([r.__dict__ for r in resultados]), 200
        except Exception as e:
            return {"erro": str(e)}, 500

    def post(self):
        try:
            json_data = request.get_json()
            resultado = UsuarioService.criar_usuario(json_data)
            return jsonify(resultado.__dict__), 201
        except ValueError as e:
            return {"erro": str(e)}, 400

class UsuarioItem(Resource):
    def get(self, usuario_id):
        try:
            resultado = UsuarioService.buscar_por_id(usuario_id)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404

    def put(self, usuario_id):
        try:
            json_data = request.get_json()
            resultado = UsuarioService.atualizar_usuario(usuario_id, json_data)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404
        except ValueError as e:
            return {"erro": str(e)}, 400

    def delete(self, usuario_id):
        try:
            resultado = UsuarioService.deletar_usuario(usuario_id)
            return jsonify(resultado), 200
        except LookupError as e:
            return {"erro": str(e)}, 404