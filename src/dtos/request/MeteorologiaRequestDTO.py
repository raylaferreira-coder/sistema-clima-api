from dataclasses import dataclass

@dataclass
class MeteorologiaRequestDTO:
    temperatura: float
    umidade: float
    descricao: str
    regiao_id: int

    def validar(self):
        erros = []
        if self.temperatura is None:
            erros.append("O campo 'temperatura' é obrigatório.")
        if self.umidade is None:
            erros.append("O campo 'umidade' é obrigatório.")
        if not self.descricao or not self.descricao.strip():
            erros.append("O campo 'descricao' é obrigatório.")
        if not self.regiao_id or self.regiao_id <= 0:
            erros.append("O campo 'regiao_id' é obrigatório e deve ser válido.")
        return erros