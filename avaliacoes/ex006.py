colab = str(input('Informe o nome do colaborador: ')).strip()
sal = float(input('Informe o salário do {}: R$'.format(colab)))
if sal < 280:
    acresc = sal * (20 / 100)
    tot = sal + acresc
    print('''
    O salário do {} antes do resjuste é R${:.2f}:
    Ele receberá um aumento de 20%, que bom!
    O aumento será de R${:.2f}
    O novo salário será R${:.2f}
    '''.format(colab, sal, acresc, tot))
elif sal >= 280 and sal < 700:
    acresc = sal * (15 / 100)
    tot = sal + acresc
    print('''
    O salário do {} antes do resjuste é R${:.2f}:
    Ele receberá um aumento de 15%, que bom!
    O aumento será de R${:.2f}
    O novo salário será R${:.2f}
    '''.format(colab, sal, acresc, tot))
elif sal >= 700 and sal < 1500:
    acresc = sal * (10 / 100)
    tot = sal + acresc
    print('''
    O salário do {} antes do resjuste é R${:.2f}:
    Ele receberá um aumento de 10%, que bom!
    O aumento será de R${:.2f}
    O novo salário será R${:.2f}
    '''.format(colab, sal, acresc, tot))
elif sal >= 1500:
    acresc = sal * (5 / 100)
    tot = sal + acresc
    print('''
    O salário do {} antes do resjuste é R${:.2f}:
    Ele receberá um aumento de 5%, que bom!
    O aumento será de R${:.2f}
    O novo salário será R${:.2f}
    '''.format(colab, sal, acresc, tot))