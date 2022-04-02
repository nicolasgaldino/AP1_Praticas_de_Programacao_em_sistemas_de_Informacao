num0 = float(input('Digite um valor qualquer: '))
num1 = float(input('Digite mais um valor qualquer: '))
opcao = str(input('''
Escolha uma das opções para realizar a operação matemática:
1 - Soma;
2 - Subtração;
3 - Multiplicação;
4 - Divisão;
''')).strip().lower()
if opcao == '1' or opcao == '1 - soma':
    tot = num0 + num1
    print('A soma entre {} e {} é: {}'.format(num0, num1, tot))
elif opcao == '2' or opcao == '2 - subtração':
    tot = num0 - num1
    print('A subtração entre {} e {} é: {}'.format(num0, num1, tot))
elif opcao == '3' or opcao == '3 - multiplicação':
    tot = num0 * num1
    print('A multiplicação entre {} e {} é: {}'.format(num0, num1, tot))
elif opcao == '4' or opcao == '4 - divisão':
    tot = num0 / num1
    print('A subtração entre {} e {} é: {:.2f}'.format(num0, num1, tot))