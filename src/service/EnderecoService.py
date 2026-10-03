from src.dtos.request.EnderecoRequestDTO import EnderecoRequestDTO
from src.dtos.response.EnderecoResponseDTO import EnderecoResponseDTO
from src.repository import EnderecoRepository

class EnderecoService:

    @staticmethod
    def listar_todos():
        enderecos = EnderecoRepository.get_all_enderecos()
        return [EnderecoResponseDTO.from_entity(e) for e in enderecos]

    @staticmethod
    def buscar_por_id(id: int):
        endereco = EnderecoRepository.get_endereco(id)
        if not endereco:
            raise LookupError(f"Endereço com id {id} não encontrado.")
        return EnderecoResponseDTO.from_entity(endereco)

    @staticmethod
    def criarEndereco(json_data: dict) -> EnderecoResponseDTO:
        dto = EnderecoRequestDTO(**json_data)
        erros = dto.validar()
        
        if erros:
            raise ValueError(f"Erros de validação: {erros}")
        
        enderecoSalvo = EnderecoRepository.add_endereco(
            cep=dto.cep,
            logradouro=dto.logradouro,
            numero=dto.numero,
            bairro=dto.bairro,
            cidade=dto.cidade,
            estado=dto.estado,
            regiao_id=dto.regiao_id
        )
        
        return EnderecoResponseDTO.from_entity(enderecoSalvo)

    @staticmethod
    def atualizarEndereco(id: int, json_data: dict) -> EnderecoResponseDTO:
        enderecoExistente = EnderecoRepository.get_endereco(id)
        
        if not enderecoExistente:
            raise LookupError(f"Endereço com id {id} não encontrado.")
        
        cep = json_data.get("cep", enderecoExistente.cep)
        logradouro = json_data.get("logradouro", enderecoExistente.logradouro)
        numero = json_data.get("numero", enderecoExistente.numero)
        bairro = json_data.get("bairro", enderecoExistente.bairro)
        cidade = json_data.get("cidade", enderecoExistente.cidade)
        estado = json_data.get("estado", enderecoExistente.estado)
        regiao_id = json_data.get("regiao_id", enderecoExistente.regiao_id)
       
        enderecoAtualizado = EnderecoRepository.update_endereco(
            id=id,
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            regiao_id=regiao_id
        )
        
        return EnderecoResponseDTO.from_entity(enderecoAtualizado)

    @staticmethod
    def deletarEndereco(id: int) -> dict:
        enderecoExistente = EnderecoRepository.get_endereco(id)
        
        if not enderecoExistente:
            raise LookupError(f"Endereço com ID {id} não encontrado.")
        
        EnderecoRepository.delete_endereco(id)
        
        return {"message": "Endereço deletado com sucesso!!!"}