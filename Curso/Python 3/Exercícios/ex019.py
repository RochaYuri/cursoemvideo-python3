import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do outro alundo: ')
aluno3 = input('Digite o nome de mais um aluno: ')
aluno4 = input('Digite o nome de um ultimo aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
sort = random.sample(alunos, 1)
print('O aluno sorteado foi: {}'.format(sort))
