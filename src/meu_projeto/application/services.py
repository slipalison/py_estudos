from meu_projeto.domain.entities import Cliente

def criar_cliente(id: int,  nome: str) -> Cliente:
    return Cliente(id=id, nome=nome)