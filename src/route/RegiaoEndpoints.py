from src.controller.RegiaoController import RegiaoList, RegiaoItem

def initialize_regiao_endpoints(api):
    api.add_resource(RegiaoList, "/regioes")
    api.add_resource(RegiaoItem, "/regioes/<int:regiao_id>")