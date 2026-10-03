from src.controller.AuditoriaController import AuditoriaList, AuditoriaItem

def initialize_auditoria_endpoints(api):
    api.add_resource(AuditoriaList, "/auditoria")
    api.add_resource(AuditoriaItem, "/auditoria/<int:auditoria_id>")