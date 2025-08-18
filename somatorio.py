import math

i=0

som = 0

n = int(input('defina quantas vezes a soma deve ocorrer:'))

while i < n:

   num=math.sqrt(i)

   print("o valor a ser somado é: ",num)

   som = som + num

   print('a soma está em ', som)

   i = i+1

print("A soma total foi: ",som)

