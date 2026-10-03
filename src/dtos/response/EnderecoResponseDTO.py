from dataclasses import dataclass
from typing import Optional

@dataclass
class EnderecoResponseDTO:
    id: int
    rua: str
    cidade: str
    cep: str
    estado: str
    numero: int
    bairro: str
    complemento: Optional[str] = None

    @classmethod
    def from_entity(cls, endereco):
        if not endereco:
            return None
        return cls(
            id=endereco.id,
            rua=endereco.rua,
            cidade=endereco.cidade,
            cep=endereco.cep,
            estado=endereco.estado,
            numero=endereco.numero,
            bairro=endereco.bairro,
            complemento=endereco.complemento
        )