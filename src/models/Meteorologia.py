from src.models.Base import Base
from sqlalchemy import Column, Integer, Float, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Meteorologia(Base):
    __tablename__ = "meteorologia"
    
    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )
    
    id_regiao = Column(
        "id_regiao",
        Integer,
        ForeignKey("regiao.id"),
        nullable=False
    )
    
    usuario_id = Column(
        "id_usuario",
        Integer,
        ForeignKey("usuario.id"),
        nullable=False
    )
    
    data = Column(
        "data",
        Date,
        nullable=False
    )
    
    temperaturaMax = Column(
        "maior_temperatura",
        Float,
        nullable=False
    )
    
    temperaturaMin = Column(
        "menor_temperatura",
        Float,
        nullable=False
    )
    
    precipitacao = Column(
        "precipitacao",
        Float,
        nullable=False
    )
    
    data_lancamento = Column(
        "data_lancamento",
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    # Relações com as respetivas tabelas
    regiao = relationship("Regiao", backref='meteorologia', lazy=True)
    usuario = relationship("Usuario", backref='meteorologia', lazy=True)