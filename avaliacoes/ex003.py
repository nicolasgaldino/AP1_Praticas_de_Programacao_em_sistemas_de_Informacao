altura = float(input('Qual a sua altura? '))
sexo = str(input('''
Digite o número da opção para escolher o sexo:
1 - Homem;
2 - Mulher;
''')).strip().lower()
if sexo == '1'or sexo == '1 - homem':
    tot = (72.7 * altura) - 58
    print('Você está pesando {:.2f}'.format(tot))
elif sexo == '2'or sexo == '2 - mulher':
    tot = (62.1 * altura) - 44.7
    print('Você está pesando {:.2f}'.format(tot))