salHora = float(input('Quanto você recebe por hora? R$'))
horaTrab = int(input('Quantas horas você trabalhou no mês? '))
salBrut = salHora * horaTrab
descIr = salBrut * (11 / 100)
descInss = salBrut * (8 / 100)
descSind = salBrut * (5 / 100)
salLiq = salBrut - (descInss + descSind + descIr)
print('''
Seu salário bruto mensal é R${:.2f}, após os descontos:
IR (11%) - R${:.2f}
INSS (8%) - R${:.2f}
Sindicato (5%) - R${:.2f}
Salário Líquido - R${:.2f}
'''.format(salBrut, descIr, descInss, descSind, salLiq))