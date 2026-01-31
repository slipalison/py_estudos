class Entidade:
    def __init__(self, id: int) -> None:
        self._id = id
    
    @property
    def id(self) -> int:
        return self._id

class Cliente(Entidade):
    def __init__(self, id: int, nome: str) -> None:
        super().__init__(id)
        self._nome = nome

    def __str__(self) -> str:
        return f"Cliente(nome={self._nome}, id={self._id})"

class Funcionario(Entidade):
    def __init__(self, id: int, cargo: str, salario: float) -> None:
        super().__init__(id)
        self._cargo = cargo
        self._salario = salario

    def __repr__(self) -> str:
        return f"Funcionario(id={self._id!r}, cargo={self._cargo!r}, salario={self._salario!r})"



c = Cliente(1, "Ana")
f = Funcionario(2, "Gerente", 10000)
print(c)
print(f)