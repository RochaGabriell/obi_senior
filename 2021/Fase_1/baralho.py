# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

cartas_baralho = input()
lista_nun_cartas = []
lista_tipos_cartas = []
copas = [True]
espadas = [True]
ouros = [True]
paus = [True]

for i in range(0, len(cartas_baralho), 3):
  lista_nun_cartas.append(cartas_baralho[i:i+2])
  lista_tipos_cartas.append(cartas_baralho[i+2:i+3])

for i in range(len(lista_nun_cartas)):
  if lista_tipos_cartas[i] == "C":
    if lista_nun_cartas[i] in copas:
      copas[0] = False
    else:
      copas.append(lista_nun_cartas[i])

  if lista_tipos_cartas[i] == "E":
    if lista_nun_cartas[i] in espadas:
      espadas[0] = False
    else:
      espadas.append(lista_nun_cartas[i])

  if lista_tipos_cartas[i] == "U":
    if lista_nun_cartas[i] in ouros:
      ouros[0] = False
    else:
      ouros.append(lista_nun_cartas[i])

  if lista_tipos_cartas[i] == "P":
    if lista_nun_cartas[i] in paus:
      paus[0] = False
    else:
      paus.append(lista_nun_cartas[i])

print(1 + (13 - len(copas))) if copas[0] == True else print("erro")
print(1 + (13 - len(espadas))) if espadas[0] == True else print("erro")
print(1 + (13 - len(ouros))) if ouros[0] == True else print("erro")
print(1 + (13 - len(paus))) if paus[0] == True else print("erro")