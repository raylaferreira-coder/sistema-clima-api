from flask import request, jsonify
from flask_restful import Resource
from src.service.AuditoriaService import AuditoriaService

class AuditoriaList(Resource):
    def get(self):
        try:
            resultados = AuditoriaService.listar_todas()
            return jsonify([r.__dict__ for r in resultados]), 200
        except Exception as e:
            return {"erro": str(e)}, 500

    def post(self):
        try:
            json_data = request.get_json()
            resultado = AuditoriaService.criarAuditoria(json_data)
            return jsonify(resultado.__dict__), 201
        except ValueError as e:
            return {"erro": str(e)}, 400

class AuditoriaItem(Resource):
    def get(self, auditoria_id):
        try:
            resultado = AuditoriaService.buscar_por_id(auditoria_id)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404

    def put(self, auditoria_id):
        try:
            json_data = request.get_json()
            resultado = AuditoriaService.atualizarAuditoria(auditoria_id, json_data)
            return jsonify(resultado.__dict__), 200
        except LookupError as e:
            return {"erro": str(e)}, 404
        except ValueError as e:
            return {"erro": str(e)}, 400

    def delete(self, auditoria_id):
        try:
            resultado = AuditoriaService.deletarAuditoria(auditoria_id)
            return jsonify(resultado), 200
        except LookupError as e:
            return {"erro": str(e)}, 404