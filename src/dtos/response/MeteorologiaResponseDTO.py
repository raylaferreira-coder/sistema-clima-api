from dataclasses import dataclass
from typing import Optional

@dataclass
class MeteorologiaResponseDTO:
    id: int
    temperatura: float
    umidade: float
    descricao: str
    regiao_id: int
    regiao_nome: Optional[str] = None 

    @classmethod
    def from_entity(cls, meteorologia):
        if not meteorologia:
            return None
        
        nome_regiao = meteorologia.regiao.nome if hasattr(meteorologia, 'regiao') and meteorologia.regiao else None

        return cls(
            id=meteorologia.id,
            temperatura=meteorologia.temperatura,
            umidade=meteorologia.umidade,
            descricao=meteorologia.descricao,
            regiao_id=meteorologia.regiao_id,
            regiao_nome=nome_regiao
        )