#1. Considere a seguinte lista de números: [2, 5, 8, 11, 14]. Escreva um programa que itere sobre
#essa lista e exiba cada número elevado ao quadrado.

listNumeros = [2,5,8,11,14]
listNumElevados=[]

for num in listNumeros:
    print(num * num)

  listNumElevados.append(num ** 2)

print(listNumElevados)