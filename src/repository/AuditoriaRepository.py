from src.models.Auditoria import Auditoria 
from src.models.Base import db

class AuditoriaRepository:
    
    @staticmethod
    def get_auditoria(id):
        return db.session.query(Auditoria).get(id)

    @staticmethod
    def get_all_auditorias():
        return db.session.query(Auditoria).all()

    @staticmethod
    def add_auditoria(acao, descricao, usuario_id, meteorologia_id, status=None, data_modificada=None):
        auditoria = Auditoria(
            acao=acao,
            descricao=descricao,
            usuario_id=usuario_id,
            meteorologia_id=meteorologia_id,
            status=status,
            dataModificada=data_modificada
        )
        
        db.session.add(auditoria)
        db.session.commit()
        db.session.refresh(auditoria)
        
        return auditoria

    @staticmethod
    def update_auditoria(id: int, acao=None, descricao=None, usuario_id=None, meteorologia_id=None, status=None, data_modificada=None):
        auditoria = db.session.query(Auditoria).get(id)
        
        if not auditoria:
            return None
            
        if acao is not None:
            auditoria.acao = acao
        if descricao is not None:
            auditoria.descricao = descricao
        if usuario_id is not None:
            auditoria.usuario_id = usuario_id
        if meteorologia_id is not None:
            auditoria.meteorologia_id = meteorologia_id
        if status is not None:
            auditoria.status = status
        if data_modificada is not None:
            auditoria.dataModificada = data_modificada
        
        db.session.commit()
        db.session.refresh(auditoria)
        return auditoria

    @staticmethod
    def delete_auditoria(id):
        auditoria = db.session.query(Auditoria).get(id)
        if auditoria:
            db.session.delete(auditoria)
            db.session.commit()
        return auditoria