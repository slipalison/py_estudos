from typing import Protocol, Optional
from .entities import Cliente


class ClienteRepository(Protocol):
    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        """Busca cliente por ID"""
        ...

    def salvar_cliente(self, cliente: Cliente) -> Cliente:
        """Salva cliente com ID auto-gerado"""
        ...

    def listar_todos(self) -> list[Cliente]:
        """Lista todos os clientes"""
        ...
