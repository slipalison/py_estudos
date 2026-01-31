idade: int = 25


if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


rang: range = range(1,7)

for item in rang:
    print(item)

print("agora lista")
lista: list = list(rang)
for item in lista:
    print(item)

frutas = ["maçã", "banana", "laranja"]
for idx, fruta in enumerate(frutas, start=1):
    print(f"{idx}. {fruta}")

scores = {"math": 100, "algo": 95, "bio": 80}
for key, value in scores.items():
    print(f"{key}: {value}")

for idx, (key, value) in enumerate(scores.items(), start=1):
    print(f"{idx}. {key}: {value}")

contador = 0
while contador <= 10:
    print(f"contador = {contador}")
    contador += 1