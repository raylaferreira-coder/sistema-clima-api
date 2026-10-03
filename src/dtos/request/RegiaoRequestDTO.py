from dataclasses import dataclass
from typing import Optional
from src.enums.tipo_regiao_enum import TipoRegiao

@dataclass
class RegiaoRequestDTO:
    nome: str
    tipo: TipoRegiao
    id_regiao: Optional[int] = None
    
    def validar(self):
        erros= []
        
        if not self.nome or len(self.nome.strip()) == 0:
            erros.append("O campo 'nome' é obrigatório")
        
        if not self.tipo:
            erros.append("O campo 'tipo' é obrigatório")
        
        return erros