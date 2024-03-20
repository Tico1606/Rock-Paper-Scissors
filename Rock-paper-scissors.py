import random

win = False

print('1 = Pedra')
print('2 = Papel')
print('3 = Tesoura')

p1 = int(input('Escolha sua opção: '))

p2 = random.randint(1, 3)


if p1 == 1:
    print('Você escolheu Pedra!')
elif p1 == 2:
    print('Você escolheu Papel!')
elif p1 == 3:
    print('Você escolheu Tesoura!')

if p2 == 1:
    print('Seu oponente escolheu Pedra!')
elif p2 == 2:
    print('Seu oponente escolheu Papel!')
elif p2 == 3:
    print('Seu oponente escolheu Tesoura!')


if p1 == 1 and p2 == 3:
    win = True
elif p1 == 2 and p2 == 1:
    win = True
elif p1 == 3 and p2 == 2:
    win = True
else:
    win = False


if win == True:
    print('Você ganhou!!')
else:
    print('Você perdeu!')
