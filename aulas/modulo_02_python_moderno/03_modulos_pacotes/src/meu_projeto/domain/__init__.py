# meu_projeto/__init__.py
from .entities import Cliente
from .cliente_repository import ClienteRepository


__all__ = ["Cliente", "ClienteRepository"]