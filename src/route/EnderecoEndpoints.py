from src.controller.AuditoriaController import AuditoriaList, AuditoriaItem
from src.controller.EnderecoController import EnderecoList, EnderecoItem

def initialize_endereco_endpoints(api):

    api.add_resource(EnderecoList, "/endereco")
    api.add_resource(EnderecoItem, "/endereco/<int:endereco_id>")
  