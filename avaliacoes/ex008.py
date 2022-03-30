'''
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for informado
um valor igual a -1 (que não deve ser armazenado). Após esta entrada de
dados, faça:
o Mostre a quantidade de valores que foram lidos;
o Exiba todos os valores na ordem em que foram informados, um ao lado
do outro;
o Exiba todos os valores na ordem inversa à que foram informados, um
abaixo do outro;
o Calcule e mostre a soma dos valores;
o Calcule e mostre a média dos valores;
o Calcule e mostre a quantidade de valores acima da média calculada;
o Calcule e mostre a quantidade de valores abaixo de sete;
o Encerre o programa com uma mensagem;
'''
notas = []
olia = notas.sort()
print('Digite -1 para encerrar o programa')
while True:
    nota = float(input('Digite a nota: '))
    if nota < 0:
        print('O programa foi encerrado')
        break
    notas.append(nota)

media = sum(notas) / len(notas)
acima = 0
abaixo = 0
for n in notas:
    if n > media:
        acima += 1
    if n < 7:
        abaixo += 1
print('Foram lidos {} valores.'.format(len(notas)))
print('Os valores lidos foram: {}'.format(notas), end='\n')
print('A soma dos valores é: %.2f' % (sum(notas)))
print('Quantidade de valores acima da média %d' % acima)
print('Quantidade de valores abaixo de sete: %d' % abaixo)