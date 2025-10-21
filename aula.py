lista_alunos = []
novo = {"nome": 'Maria', "nota": 9.2}
novo['curso'] = "Engenharia"

lista_alunos.append(novo)
novo = {"nome": 'joao', "nota": 8.2}
lista_alunos.append(novo)
print(lista_alunos[1]['nota'])

for i in range(2):
    print(lista_alunos[i]['nome'])