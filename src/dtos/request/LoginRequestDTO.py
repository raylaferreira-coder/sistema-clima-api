from dataclasses import dataclass

@dataclass
class LoginRequestDTO:
    email: str
    senha: str

    def validar(self):
        erros = []
        if not self.email or "@" not in self.email:
            erros.append("E-mail inválido.")
        if not self.senha:
            erros.append("A senha é obrigatória.")
        return erros