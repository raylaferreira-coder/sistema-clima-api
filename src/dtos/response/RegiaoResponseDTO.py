from dataclasses import dataclass
from typing import Optional

@dataclass
class RegiaoResponseDTO:
    id: int
    nome: str
    tipo: str
    id_regiao_pai: Optional[int] = None

    @classmethod
    def from_entity(cls, regiao):  # <- Faltava o 'def' aqui!
        if not regiao:
            return None
            
        tipo_valor = regiao.tipo.value if hasattr(regiao.tipo, 'value') else regiao.tipo
        
        return cls(
            id=regiao.id,
            nome=regiao.nome,
            tipo=tipo_valor,
            id_regiao_pai=regiao.id_regiao_pai
        )