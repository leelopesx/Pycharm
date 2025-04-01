#Exercicio 01

velocidade = int(input("Digite a velocidade do seu carro:"))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Infelizmente você foi multado, e a sua multa é de:", multa, "R$")
else:
    print("Você não foi multado!")

#Exercicio 02

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

print("O maior número entre eles é:",max(num1, num2, num3))
print("O menor número entre eles é:",min(num1, num2, num3))
