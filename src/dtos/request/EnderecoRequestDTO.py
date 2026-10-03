from dataclasses import dataclass
from typing import Optional

@dataclass
class EnderecoRequestDTO:
    rua: str
    cidade: str
    cep: str
    estado: str
    numero: int
    bairro: str
    complemento: Optional[str] = None

    def validar(self):
        erros = []
        if not self.rua or not self.rua.strip():
            erros.append("O campo 'rua' é obrigatório.")
        if not self.cidade or not self.cidade.strip():
            erros.append("O campo 'cidade' é obrigatório.")
        if not self.cep or not self.cep.strip():
            erros.append("O campo 'cep' é obrigatório.")
        if not self.estado or not self.estado.strip():
            erros.append("O campo 'estado' é obrigatório.")
        if not self.numero:
            erros.append("O campo 'numero' é obrigatório.")
        if not self.bairro or not self.bairro.strip():
            erros.append("O campo 'bairro' é obrigatório.")
        return erros