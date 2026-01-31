from dataclasses import dataclass
from multiprocessing.connection import Client
from typing import Literal


@dataclass
class Endereco:
    rua: str
    numero: int

@dataclass
class Cliente:
    id: int
    nome: str
    ativo: bool = True
    endereco: Endereco | None = None

    def cliente_tem_endereco(self)-> bool:
        return self.endereco is not None

@dataclass(frozen=True)
class ClienteImutavel:
    id: int
    nome: str

@dataclass
class Produto:
    id: int
    nome: str
    preco: float

    def __post_init__(self)-> None:
        if not self.nome:
            raise ValueError("Nome do produto não pode ser vazio")
        if self.preco <= 0:
            raise ValueError("Preço do produto não pode ser negativo ou zero")


@dataclass(frozen=True)
class ItemPedido:
    produto: Produto
    quantidade: int

@dataclass(frozen=True)
class Pedido:
    id: int
    cliente: ClienteImutavel
    itens: list[ItemPedido]
    status: Literal["novo", "pago", "cancelado"] = "novo"

    def total_pedido(self)-> float:
        return sum(item.produto.preco * item.quantidade for item in self.itens)


produto_1 = Produto(1, "Processador 7900X3d", 10.10)
produto_2 = Produto(2, "Memoria DDR5 2x32", 11.10)
item_pedido_1 = ItemPedido(produto_1, 1)
item_pedido_2 = ItemPedido(produto_2, 2)

pedido = Pedido(1, ClienteImutavel(1, "Ana"), [item_pedido_1, item_pedido_2])

ana = Cliente(1, "Ana")
bob = Cliente(2, "Bob", True, Endereco("Rua ABC", 123))
print(f"{ana.nome} tem endereço ? {ana.cliente_tem_endereco() }")
print(f"{bob.nome} tem endereço ? {bob.cliente_tem_endereco() }")

print(Cliente(1, "Ana"))
print(ClienteImutavel(2, "Bob"))
print(Produto(3, "Mouse", 120.50))
print(f"total: {pedido.total_pedido()}")
