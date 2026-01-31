from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str

    def validar(self)->None:
        if not self.nome:
            raise ValueError("Nome do cliente não pode ser vazio")
