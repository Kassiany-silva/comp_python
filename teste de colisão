import random
col = 0
ok = 0
for i in range(0,20):
    n = random.randint(0,1)
    if n == 0:
        ok = ok+1
        print("Sem colisão na sua mensagem")
    elif n == 1:
        col = col + 1
        print("Infelizmente sua mensagem teve colisão")

print('mensagens sem colisão:',ok)
print('mensagens com colisão:',col)
porcentagem = (col*100)/20
print("A porcentagem de colisão é:",porcentagem,'%')
