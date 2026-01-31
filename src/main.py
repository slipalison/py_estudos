from meu_projeto.application.services import criar_cliente
from meu_projeto.domain import ClienteRepository
from meu_projeto.infrastructure.repositories import ClienteRepositoryInMemory

cliente = criar_cliente(id=1, nome="João")
print(cliente)


repo: ClienteRepository = ClienteRepositoryInMemory()

repo.salvar_cliente(cliente)
repo.salvar_cliente(criar_cliente(id=2, nome="Jose"))

l = repo.listar_todos()
for c in l:
    print(c)