i = 0
k = 0
lista = []
maior = 0
vtotal=0
while i < 10:
    qtde = int(input("Digite aqui a quantidade: "))
    preco = float(input("Digite aqui o preço: "))
    descricao = input("Digite a descrição: ")
    ptotal = qtde*preco
    lista.append(ptotal)
    for l in lista:
        if ptotal > l:
            maior = descricao
    vtotal = vtotal + ptotal

    print(ptotal)
    i= i+1


print("O valor total da compra foi:",vtotal)
print("O produto com o maior valor é :",maior)
