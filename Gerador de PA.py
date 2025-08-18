#programa para mostrar os 50 primeiros termos de uma PA 
pt = int(input('Digite o valor do primeiro termo:\n'))
ra = int(input("Digite a razão:\n"))
fi = pt*50
i=0
for i in range(pt,fi,ra):
  print("Os primeiros valores da PA é:",i)
