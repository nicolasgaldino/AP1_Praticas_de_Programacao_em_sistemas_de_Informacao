nota0 = float(input('Nota do primeiro bismestre:'))
nota1 = float(input('Nota do segundo bismestre:'))
nota2 = float(input('Nota do terceiro bismestre:'))
nota3 = float(input('Nota do quarto bismestre:'))
tot = (nota0 + nota1 + nota2 + nota3) / 4
if tot < 6:
    print('Sua média é {:.2f}, infelizmnte você está reprovado.'.format(tot))
else:
    print('Sua média é {:.2f}, parabéns você foi aprovado.'.format(tot))