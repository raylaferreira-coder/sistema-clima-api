from src.controller.MeteorologiaController import MeteorologiaList, MeteorologiaItem

def initialize_meteorologia_endpoints(api):
    api.add_resource(MeteorologiaList, "/meteorologia")
    api.add_resource(MeteorologiaItem, "/meteorologia/<int:meteorologia_id>")