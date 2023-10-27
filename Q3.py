# Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
# preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
# que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.

listaCompras = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
soma = 0
for i in listaCompras:
    soma = i[1] + soma

print(soma)
