from src.models.Base import  Base 
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.enums.tipo_regiao_enum import TipoRegiao

class Regiao(Base):
    __tablename__ ="regiao"
    
    id = Column(
       "id",
       Integer,
       primary_key=True,
       autoincrement=True
    )
    
    id_regiao = Column(
        "id_regiao_pai",
        Integer, 
        ForeignKey('regiao.id'), 
        nullable=True
    )
    
    nome = Column(
        "nome",
        String(100),
        nullable=False
    )
    
    tipo = Column(
        "tipo",
        Enum(TipoRegiao),
        nullable=False
    )
    
    regioes = relationship(
        'Regiao', 
        remote_side=[id], 
        backref='regioes_segundarias', 
        lazy=True
    )