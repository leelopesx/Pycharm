#Funções
#Importando funções de outro arquivo - pode colocar o nome de cada função ou adicionar * para importar todas
from funcoes import *


a = float(input("Numero 1 ="))
b = float(input("Numero 2 ="))
print(f"Soma = {soma(a,b)}")
print(f"Soma = {subtracao(a,b)}")
print(f"Soma = {multiplicacao(a,b)}")
print(f"Soma = {divisao(a,b)}")

print(par_ou_impar(2))
print(par_ou_impar(3))

print(maior(2,4))

a = float("Digite o tamanho da base")