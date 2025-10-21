#Funções
#Importando funções de outro arquivo - pode colocar o nome de cada função ou adicionar * para importar todas
from funcoes import *


a = float(input("Numero 1 ="))
b = float(input("Numero 2 ="))
print(f"Soma = {soma(a,b)}")
print(f"Soma = {subtracao(a,b)}")
print(f"Soma = {multiplicacao(a,b)}")
print(f"Soma = {divisao(a,b)}")

print(barra(80, "."))

print(par_ou_impar(2))
print(par_ou_impar(3))

#Utiliza o * para "desempacotar" a lista
L = [5, 6]
print(soma(*L))

