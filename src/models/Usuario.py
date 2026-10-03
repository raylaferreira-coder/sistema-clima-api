from src.models.Base import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship 
from src.enums.funcao_enum import FuncaoUsuario

class Usuario(Base):
    __tablename__ = "usuario"
    
    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )
    
    id_endereco = Column(
        "id_endereco",
        Integer,
        ForeignKey("endereco.id"),
        nullable=False
    )
    
    id_regiao = Column(
        "id_regiao",
        Integer,
        ForeignKey("regiao.id"),
        nullable=False
    )
    
    nome = Column(
        "nome",
        String(150),
        nullable=False 
    )
    
    email = Column(
        "email",
        String(150),
        nullable=False,
        unique=True
    )
    
    senha = Column(
        "senha",
        String(255),
        nullable=False
    )
    
    telefone = Column(
        "telefone",
        String(15),  
        nullable=True
    )
    
    cpf = Column(
        "cpf",
        String(14),  
        nullable=False,
        unique=True
    )
    
    funcao = Column(
        "funcao",
        Enum(FuncaoUsuario, name="funcao_usuario"),
        default=FuncaoUsuario.OPERADOR,
        nullable=False
    )

    endereco = relationship('Endereco', backref='usuarios', lazy=True)
    regiao = relationship('Regiao', backref='usuarios', lazy=True)