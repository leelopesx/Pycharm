#Tuplas - são imutáveis (criada com colchetes)
tupla_alunos = ("Guilherme", "Wallace", "Pedro")
print(tupla_alunos)

a, b, c = tupla_alunos
print(b) #Print de um dos valores da tupla

nota_check = ()
print(len(nota_check))

nota_check = ("Michele",) #Adicionar vírgula, se não, é considerado str
print(len(nota_check))
print(type(nota_check))

#Transformar listas em tuplas
listas_notas = [9, 10, 5, ]
print(listas_notas)
tupla_notas = tuple(listas_notas)
print(tupla_notas)

#Soma das tuplas
notas_check1 = (6, 8, 4, 10)
notas_check2 = (7, 9, 5, 9)
total_notas = notas_check1 + notas_check2
print(total_notas)