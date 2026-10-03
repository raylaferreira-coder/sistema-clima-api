from src.dtos.request.UsuarioRequestDTO import UsuarioRequestDTO
from src.dtos.response.UsuarioResponseDTO import UsuarioResponseDTO
from src.repository.UsuarioRepository import UsuarioRepository

class UsuarioService:

    @staticmethod
    def criar_usuario(json_data: dict) -> UsuarioResponseDTO:
        dto = UsuarioRequestDTO(**json_data)
        erros = dto.validar()
        
        if erros:
            raise ValueError(f"Erros de validação: {erros}")
        
        # Instancia o repositório aqui dentro de forma segura
        usuario_salvo = UsuarioRepository.add_usuario(
            nome=dto.nome,
            cpf=dto.cpf,
            email=dto.email,
            senha=dto.senha,
            telefone=dto.telefone,
            funcao=dto.funcao
        )
        
        return UsuarioResponseDTO.from_entity(usuario_salvo)

    @staticmethod
    def atualizar_usuario(id: int, json_data: dict) -> UsuarioResponseDTO:
        usuario_existente = UsuarioRepository.get_usuario(id)
        
        if not usuario_existente:
            raise LookupError(f"Usuário com id {id} não encontrado.")
           
        nome = json_data.get("nome", usuario_existente.nome)
        cpf = json_data.get("cpf", usuario_existente.cpf)
        email = json_data.get("email", usuario_existente.email)
        senha = json_data.get("senha", usuario_existente.senha)
        telefone = json_data.get("telefone", usuario_existente.telefone)
        funcao = json_data.get("funcao", usuario_existente.funcao)

        usuario_atualizado = UsuarioRepository.update_usuario(
            id=id,
            nome=nome,
            cpf=cpf,
            email=email,
            senha=senha,
            telefone=telefone,
            funcao=funcao
        )
        
        return UsuarioResponseDTO.from_entity(usuario_atualizado)

    @staticmethod
    def deletar_usuario(id: int) -> dict:
        usuario_existente = UsuarioRepository.get_usuario(id)
        
        if not usuario_existente:
            raise LookupError(f"Usuário com ID {id} não encontrado.")
        
        UsuarioRepository.delete_usuario(id)
        
        return {"message": "Usuário deletado com sucesso!!!"}