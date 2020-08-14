import random
cards=['Hearts','Spades','Clubs','Diamonds']
face={11:'Jack',12:'Queen',13:'King'}
for _ in range(5):
    print('Your cards are')
    h=random.randint(1,4)
    n=random.randint(1,13)
    if n in list(face.keys()):print(f'{face[n]} of {cards[h]}')
    else:print(f'{n} of {cards[h]}')