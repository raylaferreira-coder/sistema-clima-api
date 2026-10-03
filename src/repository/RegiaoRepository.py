from src.models.Regiao import Regiao
from src.models.Base import db
from src.enums.tipo_regiao_enum import TipoRegiao

class RegiaoRepository:

    @staticmethod
    def get_regiao(id):
        regiao = db.session.query(Regiao).get(id)
        return regiao

    @staticmethod
    def get_all_regioes():
        return db.session.query(Regiao).all()

    @staticmethod
    def add_regiao(nome: str, tipo: TipoRegiao, id_regiao: int = None):
        regiao = Regiao(
            nome=nome,
            tipo=tipo,
            id_regiao=id_regiao
        )
        
        db.session.add(regiao)
        db.session.commit()
        db.session.refresh(regiao)
        
        return regiao
    
    @staticmethod
    def update_regiao(id: int, nome: str = None, tipo: TipoRegiao = None, id_regiao: int = None):
        regiao = db.session.query(Regiao).get(id)
        
        if not regiao:
            return None
    
        if nome is not None:
            regiao.nome = nome
        if tipo is not None:
            regiao.tipo = tipo
        if id_regiao is not None:
            regiao.id_regiao = id_regiao

        db.session.commit()
        db.session.refresh(regiao)
        return regiao
    
    @staticmethod
    def delete_regiao(id):
        regiao = db.session.query(Regiao).get(id)
        if regiao:
            db.session.delete(regiao)
            db.session.commit()
        return regiao