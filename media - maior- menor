qtda = 0
lista = []
def medias(lista , qtda):
    soma = sum(lista)
    if qtda > 0:
        media = soma/qtda
        return (media)
    else :
        return("sem valores válidos para a média!")

def maior(lista):
    n = -1
    for i in lista:
        if i > n:
            n = i
    return(n)


n = int(input("digite um número:"))
while n != 0:
    qtda = qtda + 1
    lista.append(n)
    n = int(input("digite um número:"))
    print(lista)

ma = maior(lista)
me = medias(lista,qtda)

print("O maior valor digitado foi o:",ma)
print("A média é:",me)
