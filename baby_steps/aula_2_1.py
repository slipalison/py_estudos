from typing import Optional, Union, Literal, TypedDict, Callable

UserId = int
Status = Literal["ativo", "inativo", "pendente"]

class Usuario(TypedDict):
    id: UserId
    nome: str
    status: Status

def buscar_usuario(user_id: UserId) -> Optional[Usuario]:
    if user_id == 1:
        usuario: Usuario = {"id": 1, "nome": "Ana", "status": "ativo"}
        return usuario
    return None

def processar(valor: Union[str, int]) -> str:
    return f"processado: {valor}"

def executar(callback: Callable[[int], str], valor: int) -> str:
    return callback(valor)

def cb(v: int) -> str:
    return f"valor: {v}"

print(buscar_usuario(1))
print(buscar_usuario(99))
print(processar("teste"))
print(processar(123))
print(executar(cb, 42))



class ItemPedido(TypedDict):
    nome: str
    preco: float

Id = int
PedidosStatus = Literal["novo", "pago", "cancelado"]
Item = ItemPedido

class Pedidos(TypedDict):
    id: Id
    total: float
    items: list[Item]

def formatar(status: PedidosStatus)-> str:
    label = {"novo": "Pedido Novo", "pago": "Pedido Pago" ,"cancelado": "Pedido Cancelado"}
    return label[status]

def filtrar_usuarios(usuarios: list[Usuario], status: Status) -> list[Usuario]:
    return [usuario for usuario in usuarios if usuario["status"] == status]

lista_usuario: list[Usuario] = [
    {"id": 1, "nome": "Ana", "status": "ativo"},
    {"id": 2, "nome": "Bob", "status": "inativo"},
    {"id": 2, "nome": "Cai", "status": "pendente"},
]
print(formatar("cancelado"))
print(filtrar_usuarios(lista_usuario, "pendente"))