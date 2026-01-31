from typing import Protocol

class ILogger(Protocol):
    def log_information(self, msg: str) -> None:
        """Gera um log """
        ...

    def log_debug(self, msg: str) -> None:
        """Gera um log de debug """
        ...

class LoggerConsole(ILogger):
    def log_information(self, msg: str) -> None:
        print(f"INFO: {msg}")

    def log_debug(self, msg: str) -> None:
        print(f"DEBUG: {msg!r}")


class Cliente:
    def __init__(self, id: int, nome: str) -> None:
        self.id = id
        self.nome = nome

class ClienteRepository(Protocol):
    def obter(self, id: int) -> Cliente | None: ...
    def salvar(self, cliente: Cliente) -> None: ...
    def listar(self) -> list[Cliente]: ...

class RepoMemoria:
    def __init__(self, logger: ILogger) -> None:
        self._dados: dict[int, Cliente] = {}
        self._logger = logger

    def obter(self, id: int) -> Cliente | None:
        self._logger.log_debug(f"Buscando cliente com ID {id}")
        self._logger.log_information(f"Cliente encontrado com ID {id}")
        return self._dados.get(id)

    def salvar(self, cliente: Cliente) -> None:
        self._logger.log_debug(f"Salvando cliente {cliente}")
        self._logger.log_information(f"Cliente salvo com sucesso {cliente}")
        self._dados[cliente.id] = cliente

    def listar(self) -> list[Cliente]:
        self._logger.log_debug("Listando clientes")
        self._logger.log_information(f"Total de clientes: {len(self._dados)}")
        return list(self._dados.values())




def cadastrar(repo: ClienteRepository, cliente: Cliente) -> None:
    repo.salvar(cliente)

def listar(repo: ClienteRepository) -> list[Cliente]:
    return repo.listar()

repo = RepoMemoria(LoggerConsole())
cadastrar(repo, Cliente(1, "Ana"))
print(repo.obter(1))

for c in listar(repo):
    print(c)
