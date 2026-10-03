from src.models.Meteorologia import Meteorologia 
from src.models.Base import db
from datetime import date

class MeteorologiaRepostory: 

    @staticmethod
    def get_meteorologia(id):
        return db.session.query(Meteorologia).get(id)

    @staticmethod
    def get_all_meteorologias():
        return db.session.query(Meteorologia).all()

    @staticmethod
    def add_meteorologia(id_regiao: int, usuario_id: int, data: date, temperaturaMax: float, temperaturaMin: float, precipitacao: float):
        meteorologia = Meteorologia(
            id_regiao=id_regiao,
            usuario_id=usuario_id,
            data=data,
            temperaturaMax=temperaturaMax,
            temperaturaMin=temperaturaMin,
            precipitacao=precipitacao
        )
        
        db.session.add(meteorologia)
        db.session.commit()
        db.session.refresh(meteorologia)
        
        return meteorologia
    
    @staticmethod   
    def update_meteorologia(id: int,id_regiao: int, usuario_id: int, data: date, temperaturaMax: float, temperaturaMin: float, precipitacao: float):
        meteorologia = db.session.query(Meteorologia).get(id)
        
        if not meteorologia:
            return None
    
        if data is not None:
            meteorologia.data = data
        if temperaturaMax is not None:
            meteorologia.temperaturaMax = temperaturaMax
        if temperaturaMin is not None:
            meteorologia.temperaturaMin = temperaturaMin
        if precipitacao is not None:
            meteorologia.precipitacao = precipitacao
            
        db.session.commit()
        db.session.refresh(meteorologia)
        return meteorologia
    

    @staticmethod
    def delete_meteorologia(id):
        meteorologia = db.session.query(Meteorologia).get(id)
        if meteorologia:
            db.session.delete(meteorologia)
            db.session.commit()
        return meteorologia