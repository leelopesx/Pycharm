#Dicionario: composto por conjunto de chaves e valores

alunos = {"565560": ["Anna","1ECR"], "564040":["Leticia", "1EMR"]}
print(alunos)

#Alterar valor
alunos["564040"][1] = "1ECR"
print(alunos)

#Exibir apenas o valor desejado
print(alunos["564040"])

#Consulta
print("565560" in alunos)
print("565561" in alunos)

#Exibe as chaves do dicionário
print(alunos.keys())

#Exibe os valores do dicionário
print(alunos.values())

#Exercicío 01
#desafio - vagas (subtrair cada vez que o usuário entrar, e diminuir do "estoque)
cursos = {"engenharia de software": ["R$2680.00" , "4 anos", 5 ],
          "engenharia da computação": ["R$2680.00", "4 anos", 4] ,
          "engenharia mecatrônica": ["R$2135.00", "5 anos", 3 ]}

while True:
    curso = input("Digite o curso desejado (ou fim para encerrar):").lower()  #Lower - transforma tudo em minusculo
    if curso in cursos:
        custo = cursos[curso][0]
        duracao = cursos[curso][1]
        vagas = cursos[curso][2]
        print(f"O curso {curso} tem o valor de R$  {custo}  mensal, com uma duração de {duracao}, e com apenas {vagas} vagas." )
        resposta = input("Você deseja fazer a sua matrícula?")

        if resposta == "sim":
            if cursos[curso][2] > 0:
                cursos[curso][2] -= 1
                print(f"Parabéns, você está matriculado no curso {curso}!!")

            else:
                print("Infelizmente não há mais vagas nesse curso!")

    elif curso == "fim":
        print("Busca encerrada")
        break

    else:
        print("O curso desejado não foi encontrado")

#Exemplo
estoque = {"tomate": [1000, 2.3], "alface": [500, 0.45], "batata": [2001, 1.2], "feijão": [100, 1.5]} #dicionário
venda = [["tomate", 5], ["batata", 10], ["alface", 5]] #valores vendidos
total = 0
for operacao in venda:
    produto, quantidade = operacao #atribuindo nomes para os elementos da lista
    preco = estoque[produto][1] #definindo onde está o valor no dicionário
    custo = preco * quantidade
    print(f"{produto}: {quantidade} x {preco} = {custo}")
    estoque[produto][0] -= quantidade #retirar quantidade do estoque
    total += custo

print(f"Custo total: {total}")

for chave, dados in estoque.items(): #exibe todos os valores / items - separa os valores dentro da chave
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: R$ {dados[1]}")





