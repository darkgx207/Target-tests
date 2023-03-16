print(''' ========= Bem vindo =========
Este script verifica se um dado numero pertence ou não a sequencia de fibonacci.\n''')

targetNumber = int(input('Digite o valor que deseja verificar: '))

a = 0
b = 1

while True:
    c = b
    b = a + b
    a = c
    if b == targetNumber:
        print('Este numero pertence a sequencia de fibonacci')
        break
    if b > targetNumber:
        print('Este numero não pertence a sequencia de fibonacci')
        break