#Strings - não é possível mudar algum caracter da string
frase = "Hello World"
print(frase)
print(len(frase))
print(frase[0])
print(frase[-1]) #Mostra o último caracter da frase

#Soma das strings
string1 = "Hello"
string2 = "World"
print(string1+string2)
print(string1,string2) #Junção das palavras
string3 = "!"
print(string1,string2, string3*3)
print()

#tranformar string em lista
frase = list("Hello World")
print(lista_frase)

#join - operação inversa
frase = "".join() #Se deixar espaço nas aspas, a string fica toda separada

#Verificando os primeiros ou os últimos caracteres da string
print(frase.startswith("Hello"))
print(frase.endswith("!"))

#In - está dentro da frase?
print("Z" in frase)

#Count - contagem de caracteres escolhido
print(frase.count("o"))

#Find - mostra se tem o caractere escolhido e sua posição (se aparecer -1, é pq não existe)
print(frase.find("e"))

#Ajuste
print(frase.center(30)) #no centro (30 - o espaço todo)
print(frase.center(30,"-"))

print(frase.ljust(50,"-")) #esquerda
print(frase.rjust(50,"-")) #direita

#Split - quebra uma string
print(frase.split()) #Pode indicar onde quer quebrar
print(frase)

frase_quebrada = frase.split()
print(frase_quebrada)

#Renomear
print(frase.replace("World", "mundo"))
nova_frase = frase.replace("World", "mundo")
print(nova_frase)
print(frase)

#Pular linha
print("Olá mundo", end="\n\n") #2 linhas
print("Oi")

#Separação
print('Hello', "World")
print('Hello', "World", sep=' ')
print('Hello', "World", sep=',')
print('Hello', "World", sep="," , end="!")