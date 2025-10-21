#Def - definir o que é uma função
def soma(a, b):
    return a+b

def subtracao (a,b):
    return a-b

def multiplicacao (a,b):
    return a*b

def divisao (a,b):
    return a/b

def ehpar(x):
 return x % 2 == 0

def par_ou_impar(x):
 if ehpar(x):
    return "par"
 else:
    return "ímpar"

def maior(a,b):
    if a > b:
        return a
    else:
        return b

#Parametros opcionais, e caso for combinar com parâmetros obrigatórios, os opcionais devem ser os últimos
def barra(n=40,caractere="*"):
    return n*caractere