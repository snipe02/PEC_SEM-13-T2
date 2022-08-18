lucas = []

while True:
    y = int(input())
    if y!=0:
        lucas.append(y)
    if y == 0:
        break


def len_contador(n):
    cont = 0
    for c in n:
        cont += 1
    return cont

def inverso(n):
    lista_inversa = []
    for c in n:
        lista_inversa.insert(0, c)
    return lista_inversa

def menor_func(n):
    menor = 9999999999999999
    for c in n:
        if c < menor:
            menor = c
    return menor

def maior_func(n):
    maior = -999999999
    for c in n:
        if c > maior:
            maior = c
    return maior

def suma_func(n):
    soma = 0
    for c in n:
        soma += c
    return soma


print(lucas)
print(len_contador(lucas))
print(inverso(lucas))
print(menor_func(lucas))
print(maior_func(lucas))
print(sum(lucas))






