from dataclasses import dataclass
from typing import Protocol

@dataclass
class Cliente:
    nome: str
    id: int

    def __str__(self) -> str:
        return f"Cliente -> id:{self.id} nome:{self.nome}"


class ClienteRepository(Protocol):
    def get_by_id(self, id: int) -> Cliente | None: ...
    def save(self, cliente: Cliente) -> None: ...
    def listar(self) -> list[Cliente]: ...
    def contar(self) -> int: ...

class ClienteRepositoryMemoria:
    def __init__(self) -> None:
        self._store: dict[int, Cliente] = {}

    def get_by_id(self, id: int) -> Cliente | None:
        return self._store.get(id)

    def save(self, cliente: Cliente) -> None:
        self._store[cliente.id] = cliente
    def listar(self) -> list[Cliente]:
        return list(self._store.values())
    def contar(self) -> int:
        return len(self._store)

def criar_cliente(nome: str, repo: ClienteRepository) -> Cliente:
    return Cliente(nome=nome, id=repo.contar() + 1)

#strategy
class DescontoStrategy(Protocol):
    def calcular(self, valor: float) -> float: ...

class DescontoPadrao:
    def calcular(self, valor: float) -> float:
        return valor * 0.9

def aplicar_desconto(valor: float, desconto: DescontoStrategy) -> float:
    return desconto.calcular(valor)

repo = ClienteRepositoryMemoria()
cliente = criar_cliente("Ana",repo)
repo.save(cliente)
cliente2 = criar_cliente("Bob",repo)
repo.save(cliente2)
print(repo.get_by_id(cliente.id))
print(repo.get_by_id(cliente2.id))
print(aplicar_desconto(100, DescontoPadrao()))