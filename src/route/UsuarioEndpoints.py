from src.controller.UsuarioController import UsuarioList, UsuarioItem

def initialize_usuario_endpoints(api):
   
    api.add_resource(UsuarioList, "/usuario")
    api.add_resource(UsuarioItem, "/usuario/<int:usuario_id>")