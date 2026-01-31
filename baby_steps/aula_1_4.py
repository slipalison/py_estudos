def calcular_desconto(valor: float, percentual: float = 0.1) -> float:
    return valor * (1- percentual)

def saudacao(nome: str, titulo: str|None = None) -> str:
    if titulo:
        return f"Ola, {titulo} {nome}"
    return f"Ola, {nome}"

# void Somar(params int[] numeros) { ... }
def somar(*numeros: int)-> int:
    return sum(numeros)

# void Config(Dictionary<string, object> opcoes) { ... }
def montar_config(**opcoes: str) -> dict[str, str]:
    return opcoes

print(calcular_desconto(100))
print(calcular_desconto(200, 0.2))
print(saudacao("Ana"))
print(saudacao("Ana", "Dra."))
print(somar(1, 2, 3, 4))
print(montar_config(ambiente="dev", log="info"))