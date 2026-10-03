from src.models.Base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from src.enums.status_enum import StatusSolicitacao

class Auditoria(Base):
    __tablename__ = "auditoria"
    
    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )
    
    usuario_id = Column(
        "id_usuario",
        Integer,
        ForeignKey('usuario.id'), 
        nullable=False
    )
    
    meteorologia_id = Column(
        "id_meteorologia",
        Integer,
        ForeignKey('meteorologia.id'),
        nullable=False
    )
    
    dataModificada = Column(
        "data_modificacao",
        DateTime,
        nullable=True
    )
    
    descricao = Column(
        "descricao",
        Text,
        nullable=False
    )
    
    status = Column(
        "status",
        Enum(StatusSolicitacao),
        default=StatusSolicitacao.PENDENTE,
        nullable=False
    )

  
    usuario = relationship(
        'Usuario', 
        backref='auditorias', 
        lazy=True
    )
    
    meteorologia = relationship(
        'Meteorologia',
        backref='auditorias',
        lazy=True
    )