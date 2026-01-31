from __future__ import annotations
from typing import Optional

nome: str = "joão"
idade: int = 25
ativo: bool = True
peso: float = 80.5
apelido: Optional[str] = None # nullable seria um Nullable<T> no c#
apelido2: str | None = None # nullable seria um string?  no c#

tags: list[str] = ["python", "curso"]
scores: dict[str, int] = {"math": 100, "algo": 95}
coords: tuple[int, int] = (10, 20)
unique_ids: set[int] = {1, 2, 3} # é equivalente ao HashSet<T> do C#

print(type(nome), type(idade), type(ativo), type(peso), type(apelido), type(apelido2), type(tags), type(scores), type(coords), type(unique_ids))
print(apelido is None)
print(f"Nome: {nome}, Idade: {idade}, Ativo: {ativo}, Peso: {peso}, Apelido: {apelido}")
print(scores.get("math"), scores.get("bio", 0))