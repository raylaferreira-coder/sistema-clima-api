from src.models.Base import db
from src.models.Usuario import Usuario
from src.enums.funcao_enum import FuncaoUsuario

class UsuarioRepository:
    
    @staticmethod
    def get_usuario(id):
        usuario = db.session.query(Usuario).get(id)
        return usuario

    @staticmethod
    def get_all_usuarios():
        return db.session.query(Usuario).all()

    @staticmethod
    def add_usuario(nome: str, cpf: int, email: str, senha: str, telefone: int, funcao: FuncaoUsuario):
        usuario = Usuario(
            nome=nome,
            cpf=cpf,
            email=email,
            senha=senha,
            telefone=telefone,
            funcao=funcao
        )
        
        db.session.add(usuario)
        db.session.commit()
        db.session.refresh(usuario)
        
        return usuario
        
    @staticmethod
    def update_usuario(id: int, nome: str, cpf: int, email: str, senha: str, telefone: int, funcao: FuncaoUsuario):
        usuario = db.session.query(Usuario).get(id)
        if not usuario:
            return None
            
        usuario.nome = nome
        usuario.cpf = cpf
        usuario.email = email
        usuario.senha = senha
        usuario.telefone = telefone
        usuario.funcao = funcao
        
        db.session.commit()
        db.session.refresh(usuario)
        return usuario

    @staticmethod
    def delete_usuario(id):
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        return usuario