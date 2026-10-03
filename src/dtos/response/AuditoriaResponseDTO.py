from dataclasses import dataclass
from typing import Optional

@dataclass
class AuditoriaResponseDTO:
    id: int
    data_modificacao: str
    acao: str
    usuario_id: int
    usuario_nome: Optional[str] = None  

    @classmethod
    def from_entity(cls, auditoria):
        if not auditoria:
            return None
        
        data_formatada = auditoria.dataModificada.isoformat() if auditoria.dataModificada else None
        
        nome_usuario = auditoria.usuario.nome if hasattr(auditoria, 'usuario') and auditoria.usuario else None

        return cls(
            id=auditoria.id,
            data_modificacao=data_formatada,
            acao=auditoria.acao,
            usuario_id=auditoria.usuario_id,
            usuario_nome=nome_usuario
        )
