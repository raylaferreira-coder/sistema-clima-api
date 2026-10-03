from dataclasses import dataclass

@dataclass
class UsuarioResponseDTO:
    id: int
    nome: str
    email: str
    funcao: str

    @classmethod
    def from_entity(cls, usuario):
        if not usuario:
            return None
        
        funcao_valor = usuario.funcao.value if hasattr(usuario.funcao, 'value') else usuario.funcao

        return cls(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            funcao=funcao_valor
        )