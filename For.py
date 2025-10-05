#Aprendendo a usar o for - estrutura de repetição

#Exercicio 01
lista_produtos = ["iphone", "ipad", "macbook"]

for produto in lista_produtos:
    print(produto)

#Exercicio 02
print("Seja bem vindo!")
n1 = int(input("Digite o 1° número:"))
n2 = int(input("Digite o 2° número:"))
n3 = int(input("Digite o 3° número:"))
numeros = [n1, n2, n3]
maior = numeros[0]
menor = numeros[0]
posicao = 0
posicao1 = 0
for i in range (len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i
    if numeros[i] < menor:
        menor = numeros[i]
        posicao1 = i

print(f"A soma dos número é igual a {sum(numeros)}")
print(f"O maior número é {maior}, na posição {posicao+1} e o menor é {menor}, na posição {posicao1+1}")

#Exercicio 03
vogais = 0
for letras in str(input("Digite uma frase:")).lower():
    if letras in "aeiou": #Não reconhece vogais com acento
        vogais += 1

print(f"Nessa frase tem {vogais} vogais")