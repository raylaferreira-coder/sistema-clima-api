from src.dtos.request.MeteorologiaRequestDTO import MeteorologiaRequestDTO
from src.dtos.response.MeteorologiaResponseDTO import MeteorologiaResponseDTO
from src.repository import MeteorologiaRepository


class MeteorologiaService:

    @staticmethod
    def listar_todas():
        meteorologias = MeteorologiaRepository.get_all_meteorologias()
        return [MeteorologiaResponseDTO.from_entity(m) for m in meteorologias]

    @staticmethod
    def buscar_por_id(id: int):
        meteorologia = MeteorologiaRepository.get_meteorologia(id)
        if not meteorologia:
            raise LookupError(f"Meteorologia com id {id} não encontrada.")
        return MeteorologiaResponseDTO.from_entity(meteorologia)

    @staticmethod
    def criarMeteorologia(json_data: dict) -> MeteorologiaResponseDTO:
        dto = MeteorologiaRequestDTO(**json_data)
        erros = dto.validar()
        
        if erros:
            raise ValueError(f"Erros de validação: {erros}")
        
        meteorologiaSalvo = MeteorologiaRepository.add_meteorologia(
            id_regiao=dto.id_regiao,
            usuario_id=dto.usuario_id,
            data=dto.data,
            temperaturaMax=dto.temperaturaMax,
            temperaturaMin=dto.temperaturaMin,
            precipitacao=dto.precipitacao
        )
        
        return MeteorologiaResponseDTO.from_entity(meteorologiaSalvo)

    @staticmethod
    def atualizarMeteorologia(id: int, json_data: dict) -> MeteorologiaResponseDTO:
        meteorologiaExistente = MeteorologiaRepository.get_meteorologia(id)
        
        if not meteorologiaExistente:
            raise LookupError(f"Meteorologia com id {id} não encontrada.")
        
        data = json_data.get("data", meteorologiaExistente.data)
        temperaturaMax = json_data.get("temperaturaMax", meteorologiaExistente.temperaturaMax) 
        temperaturaMin = json_data.get("temperaturaMin", meteorologiaExistente.temperaturaMin) 
        precipitacao = json_data.get("precipitacao", meteorologiaExistente.precipitacao) 
       
        meteorologiaAtualizado = MeteorologiaRepository.update_meteorologia(
            id=id,
            data=data,
            temperaturaMax=temperaturaMax,
            temperaturaMin=temperaturaMin,
            precipitacao=precipitacao
        )
        
        return MeteorologiaResponseDTO.from_entity(meteorologiaAtualizado)

    @staticmethod
    def deletarMeteorologia(id: int) -> dict:
        meteorologiaExistente = MeteorologiaRepository.get_meteorologia(id)
        
        if not meteorologiaExistente:
            raise LookupError(f"Meteorologia com ID {id} não encontrada.")
        
        MeteorologiaRepository.delete_meteorologia(id)
        
        return {"message": "Meteorologia deletada com sucesso!!!"}