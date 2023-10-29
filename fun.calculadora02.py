def calculadora(n1, n2, op):
    if op == 1:
        return n1 + n2
    elif op == 2:
        return n1 - n2
    elif op == 3:
        return n1 * n2
    elif op == 4:
        return n1 / n2
    else:
        return calculadora
        
opcao = 1
while opcao:
    print('')
    print('LISTA DE OPERAÇÕES:')
    print('')
    print('1: Soma')
    print('2: Subtração')
    print('3: Multiplicação')
    print('4: Divisão')
    print('0: Sair')
    print('')
    
    opcao = int(input('Escolha uma das seguintes opções acima: '))
    if opcao == 0:
        break
    elif opcao > 4:
        print('Essa operação não existe')
        continue

    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro: '))
    operacao = int(input('Digite o operador: '))
    if operacao > 4:
        print(f'A operação {operacao} não existe!')
        continue
    res = calculadora(n1, n2, operacao)
    print(f'O resultado de {n1} e {n2} é {res}!')