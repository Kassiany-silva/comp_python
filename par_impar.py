'''Crie um programa que leia uma quantidade não determinada de
números inteiros. O programa deve calcular e escrever a quantidade
de números pares e ímpares e a média aritmética dos números pares.
A leitura deve ser encerrada quando for lido o número zero, que não
deve ser considerado.'''

pares=[]
p = 0
i=0
n = int(input("Digite um número:"))
while n != 0:
    if n%2 == 0:
        p = p+1
        pares.append(n)
    else:
        i=  i+1
    n = int(input("Digite um número:"))

media = sum(pares)/p
print('A quantidade de números pares foi:',p)
print('A quantidade de números impares foi:',i)
print("A média aritimética dos numeros pares é:",media)


