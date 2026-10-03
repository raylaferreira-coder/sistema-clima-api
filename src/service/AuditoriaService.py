from src.dtos.request.AuditoriaRequestDTO import AuditoriaRequestDTO
from src.dtos.response.AuditoriaResponseDTO import AuditoriaResponseDTO
from src.repository.AuditoriaRepository import AuditoriaRepository

class AuditoriaService:

    @staticmethod
    def listar_todas():
        auditorias = AuditoriaRepository.get_all_auditorias()
        return [AuditoriaResponseDTO.from_entity(a) for a in auditorias]

    @staticmethod
    def buscar_por_id(id: int):
        auditoria = AuditoriaRepository.get_auditoria(id)
        if not auditoria:
            raise LookupError(f"Auditoria com id {id} não encontrada.")
        return AuditoriaResponseDTO.from_entity(auditoria)

    @staticmethod
    def criarAuditoria(json_data: dict) -> AuditoriaResponseDTO:
        dto = AuditoriaRequestDTO(**json_data)
        erros = dto.validar()
        
        if erros:
            raise ValueError(f"Erros de validação: {erros}")
        
        auditoriaSalva = AuditoriaRepository.add_auditoria(
            acao=dto.acao,
            descricao=dto.descricao,
            usuario_id=dto.usuario_id,
            meteorologia_id=getattr(dto, 'meteorologia_id', None),
            status=getattr(dto, 'status', None),
            data_modificada=getattr(dto, 'data_modificada', None)
        )
        
        return AuditoriaResponseDTO.from_entity(auditoriaSalva)

    @staticmethod
    def atualizarAuditoria(id: int, json_data: dict) -> AuditoriaResponseDTO:
        auditoriaExistente = AuditoriaRepository.get_auditoria(id)
        
        if not auditoriaExistente:
            raise LookupError(f"Auditoria com id {id} não encontrada.")
        
        acao = json_data.get("acao", auditoriaExistente.acao)
        descricao = json_data.get("descricao", auditoriaExistente.descricao)
        usuario_id = json_data.get("usuario_id", auditoriaExistente.usuario_id)
        meteorologia_id = json_data.get("meteorologia_id", auditoriaExistente.meteorologia_id)
        status = json_data.get("status", auditoriaExistente.status)
        data_modificada = json_data.get("data_modificada", auditoriaExistente.dataModificada)
       
        auditoriaAtualizada = AuditoriaRepository.update_auditoria(
            id=id,
            acao=acao,
            descricao=descricao,
            usuario_id=usuario_id,
            meteorologia_id=meteorologia_id,
            status=status,
            data_modificada=data_modificada
        )
        
        return AuditoriaResponseDTO.from_entity(auditoriaAtualizada)

    @staticmethod
    def deletarAuditoria(id: int) -> dict:
        auditoriaExistente = AuditoriaRepository.get_auditoria(id)
        
        if not auditoriaExistente:
            raise LookupError(f"Auditoria com ID {id} não encontrada.")
        
        AuditoriaRepository.delete_auditoria(id)
        
        return {"message": "Auditoria deletada com sucesso!!!"}