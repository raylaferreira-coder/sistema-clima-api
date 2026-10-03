from dataclasses import dataclass

@dataclass
class AuditoriaRequestDTO:
    acao: str
    usuario_id:int
    
    def validar(self):
        erros = []
        
        if not self.acao or len(self.acao.strip())==0:
            erros.append("O campo é obrigatório.")
            
        if not self.usuario_id or self.usuario_id <=0:
            erros.append("O campo usuário é obrigatório")
            
        return erros