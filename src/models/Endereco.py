from src.models.Base import Base
from sqlalchemy import Column, Integer, String

class Endereco(Base):
    __tablename__ = 'endereco'
    
    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )
    
    rua = Column(
        "rua",
        String(255),
        nullable=False
    )
    
    cidade = Column(
        "cidade",
        String(100),
        nullable=False
    )
    
    cep = Column(
        "cep",
        String(10),
        nullable=False
    )
    
    estado = Column(
        "estado",
        String(2),
        nullable=False
    )
    
    complemento = Column(
        "complemento",
        String(100),
        nullable=True
    )
    
    numero = Column(
        "numero",
        Integer,
        nullable=False
    ) 
     
    bairro = Column(
        "bairro",
        String(100),
        nullable=False
    )