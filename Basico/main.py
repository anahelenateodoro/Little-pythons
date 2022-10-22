import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Advinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, advinhe novamente. Muito baixo.')
        elif guess > random_number:
            print('Deesculpe, advinhe novamente. Muito alto.')

    print(f'Eba, parabéns. Você advinhou o númer{random_number}, corretooo!!!')

guess(100)