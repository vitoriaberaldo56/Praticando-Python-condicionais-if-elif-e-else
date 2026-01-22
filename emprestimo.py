# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
#
# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

Renda = float(input('Digite a sua renda mensal: '))
Parcela = int(input('Digite o valor da parcela desejada: '))
LimiteParcela = Renda * 0.30


if Renda > 2000:
    if Parcela > LimiteParcela:
        print('Empréstimo negado: parcela acima de 30% da renda.')
    else:
        print('Empréstimo aprovado!')
else:
    print('Renda abaixo do mínimo')