#peograma que calcula a média salarial de homemns mulheres e o maior salário dos mais novos que 30 anos.
#declaração de variaveis
lista=[]

salf = 0 
salm = 0
qtf = 0 
qtm =0 
menos =[]
#solicitando infromações
idade = int(input("digite sua idade:"))
while idade >=0:
  lista.append(idade)
   sexo=input("digite 'M' para masculino e 'F'para feminino")
  salario= float(input("Digite seu sálario"))
  if idade <= 30:
    menos.append(salario)
  s = sexo.upper()
  if s =='F':
    salf = salario + salf
    qtf = qtf+ 1
  elif s == 'M':
    salm = salario + salm
    qtm = qtm+1 
    
  idade = int(input("digite sua idade:"))
maior = max(menos)
medf = salf / qtf
medm = salm / qtm
print("A média salarial feminina é:",medf)
print("A média salarial masculina é:",medm)
print("O maior salário do mais novo é:", maior)
