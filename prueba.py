import uuid
lista = ["asdassd"]
personal = str(uuid.uuid4())[:8]
print(lista)
for a in lista:
    if a != personal:
        lista.append(personal)
        

print(lista)

personal = str(uuid.uuid4())[:8]
encontrado = False
indice = 0

longitud = len(str(202041390))
print(longitud)
while not encontrado and indice<longitud:
    print(lista[indice])
    print(personal)

    if lista[indice] != personal:
        encontrado = True
        lista.append(personal)
    else:
        indice +=1

    
print(lista)