numeros = list(range(1, 11))

# list comprehension (pares * 2)
pares_dobrados = [numero * 2 for numero in numeros if numero % 2 == 0]

# dict comprehension (quadrados)
quadrados = {n: n**2 for n in numeros}

# set comprehension (restos mod 3)
restos = {n % 3 for n in numeros}

# zip para criar dict
nomes = ["ana", "bob", "cai"]
idades = [28, 35, 22]
pessoas = {nome: idade for nome, idade in zip(nomes, idades)}


print(pares_dobrados)
print(quadrados)
print(restos)
print(pessoas)


def to_upper(*textos: str) -> list[str]:
    return [t.upper() for t in textos]

print(to_upper("ana", "bob", "cai"))

cubos = {n: n**3 for n in numeros if n % 2 != 0}
print(cubos)

list_duplicada =[1,2,3,3,4,5,6,6,6,7,8,8,9,0]
print(list(set(list_duplicada)))

frases = ["ola mundo", "python é top!", "c# vs python"]
lens= [len(f.split()) for f in frases]
print(lens)
print({frase:length for frase, length in zip(frases, lens)})