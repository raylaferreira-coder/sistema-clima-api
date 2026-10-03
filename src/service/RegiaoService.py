from src.dtos.request.RegiaoRequestDTO import RegiaoRequestDTO
from src.dtos.response.RegiaoResponseDTO import RegiaoResponseDTO
from src.repository.RegiaoRepository import RegiaoRepository

class RegiaoService:

    @staticmethod
    def listar_todas():
        regioes = RegiaoRepository.get_all_regioes()
        return [RegiaoResponseDTO.from_entity(r) for r in regioes]

    @staticmethod
    def buscar_por_id(id: int):
        regiao = RegiaoRepository.get_regiao(id)
        if not regiao:
            raise LookupError(f"Região com id {id} não encontrada.")
        return RegiaoResponseDTO.from_entity(regiao)

    @staticmethod
    def criarRegiao(json_data: dict) -> RegiaoResponseDTO:
        dto = RegiaoRequestDTO(**json_data)
        erros = dto.validar()
        
        if erros:
            raise ValueError(f"Erros de validação: {erros}")
        
        regiaoSalva = RegiaoRepository.add_regiao(
            nome=dto.nome,
            tipo=dto.tipo,
            id_regiao=getattr(dto, 'id_regiao', getattr(dto, 'id_regiao_pai', None))
        )
        
        return RegiaoResponseDTO.from_entity(regiaoSalva)

    @staticmethod
    def atualizarRegiao(id: int, json_data: dict) -> RegiaoResponseDTO:
        regiaoExistente = RegiaoRepository.get_regiao(id)
        
        if not regiaoExistente:
            raise LookupError(f"Região com id {id} não encontrada.")
        
        nome = json_data.get("nome", regiaoExistente.nome)
        tipo = json_data.get("tipo", regiaoExistente.tipo)
        id_regiao = json_data.get("id_regiao", json_data.get("id_regiao_pai", regiaoExistente.id_regiao))
        
        regiaoAtualizada = RegiaoRepository.update_regiao(
            id=id,
            nome=nome,
            tipo=tipo,
            id_regiao=id_regiao
        )
        
        return RegiaoResponseDTO.from_entity(regiaoAtualizada)

    @staticmethod
    def deletarRegiao(id: int) -> dict:
        regiaoExistente = RegiaoRepository.get_regiao(id)
        
        if not regiaoExistente:
            raise LookupError(f"Região com ID {id} não encontrada.")
        
        RegiaoRepository.delete_regiao(id)
        
        return {"mensagem": f"Região com ID {id} deletada com sucesso."}