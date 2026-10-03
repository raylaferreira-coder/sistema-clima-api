from src.models.Endereco import Endereco
from src.models.Base import db

class EnderecoRepository: 
    
    @staticmethod
    def get_endereco(id):
        return db.session.query(Endereco).get(id)

    @staticmethod
    def get_all_enderecos():
        return db.session.query(Endereco).all()

    @staticmethod
    def add_endereco(cep, logradouro, numero, bairro, cidade, estado, regiao_id):
        endereco = Endereco(
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            regiao_id=regiao_id
        )
        
        db.session.add(endereco)
        db.session.commit()
        db.session.refresh(endereco)
        
        return endereco
    
    @staticmethod  
    def update_endereco(id: int, cep=None, logradouro=None, numero=None, bairro=None, cidade=None, estado=None, regiao_id=None):
        endereco = db.session.query(Endereco).get(id)
        
        if not endereco:
            return None
            
        if cep is not None:
            endereco.cep = cep
        if logradouro is not None:
            endereco.logradouro = logradouro
        if numero is not None:
            endereco.numero = numero
        if bairro is not None:
            endereco.bairro = bairro
        if cidade is not None:
            endereco.cidade = cidade
        if estado is not None:
            endereco.estado = estado
        if regiao_id is not None:
            endereco.regiao_id = regiao_id
        
        db.session.commit()
        db.session.refresh(endereco)
        return endereco

    @staticmethod
    def delete_endereco(id):
        endereco = db.session.query(Endereco).get(id)
        if endereco:
            db.session.delete(endereco)
            db.session.commit()
        return endereco