from typing import Optional, List

from meu_projeto.domain.entities import Cliente
from meu_projeto.domain.cliente_repository import ClienteRepository


class ClienteRepositoryInMemory(ClienteRepository):
    def __init__(self):
        self._clientes: List[Cliente] = []

    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        for cliente in self._clientes:
            if cliente.id == cliente_id:
                return cliente
        return None

    def salvar_cliente(self, cliente: Cliente) -> Cliente:
        if self._clientes:
            proximo_id = max(c.id for c in self._clientes) + 1
        else:
            proximo_id = 1

        cliente_com_id = Cliente(id=proximo_id, nome=cliente.nome)
        self._clientes.append(cliente_com_id)
        return cliente_com_id

    def listar_todos(self) -> List[Cliente]:
        return self._clientes.copy()
