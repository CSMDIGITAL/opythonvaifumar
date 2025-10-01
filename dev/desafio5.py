"""
 Cadastrar um produto e descobrir o valor total
"""
import math

# string [e] texto
produto = input("Digite o nome do produto")
qtde = int(input("Digite a quantidade de produto"))
preco = float(input("Digite o valor do produto"))
total = qtde * preco
print('o valor total:', total)  # concatenar
print(f'o produto {produto} tem o valor total de {total}')  # interpolar

# Estrutura Condicional
# Se o valor total for maior que 1000 entao de um desconto de 10
# >  < ==
if total >= 1000:
    print("o valor total é maior ou igual a 1000")

math.pow(2,2)
# 2 base
# 2 expoente
# 2²
math.sqrt()
