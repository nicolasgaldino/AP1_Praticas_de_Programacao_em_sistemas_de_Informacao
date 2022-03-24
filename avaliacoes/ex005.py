nota0 = float(input('Digita a nota do primeiro bimestre: '))
nota1 = float(input('Digita a nota do segundo bimestre: '))
tot = (nota0 + nota1) / 2
if tot >= 7 and tot <= 9.9:
    print('Com a média {:.2f}, você está aprovado. Parabéns!'.format(tot))
elif tot < 7:
    print('Com a média {:.2f}, você está reprovado.'.format(tot))
if tot == 10:
    print('Com a média {:.2f}, você foi aprovado com distinção. Parabéns!'.format(tot))