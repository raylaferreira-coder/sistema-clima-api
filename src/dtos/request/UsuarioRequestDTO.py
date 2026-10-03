from dataclasses import dataclass
from typing import Optional
from src.enums.funcao_enum import FuncaoUsuario

@dataclass
class UsuarioRequestDTO:
    nome: str
    email: str
    senha: str
    funcao: Optional[FuncaoUsuario] = FuncaoUsuario.OPERADOR

    def validar(self):
        erros = []
        if not self.nome or not self.nome.strip():
            erros.append("O campo 'nome' é obrigatório.")
        if not self.email or "@" not in self.email:
            erros.append("Um e-mail válido é obrigatório.")
        if not self.senha or len(self.senha) < 6:
            erros.append("A senha é obrigatória e deve ter pelo menos 6 caracteres.")
        return erros