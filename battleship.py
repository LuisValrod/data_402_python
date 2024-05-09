from pokemons import pokemons
from attacks import attack

def battle(p1, p2):
    pl1=p1
    pl2=p2
    print(f"The first contestan's pokemon is {p1} and the second contestan's pokemon is {p2}")
    print(f"{pl1}'s speed is {pokemons[pl1]['Stats']['spd. attack']}")
    print(f"{pl2}'s speed is {pokemons[pl2]['Stats']['spd. attack']}")
    if pokemons[p2]['Stats']['spd. attack'] > pokemons[p1]['Stats']['spd. attack']:
        pl1, pl2 = pl2, pl1
    print(f'Therefore, the first move is for {pl1}')
    while True:
        attack(pl1, pl2)
        # print(f'{pl1} attacked with {move}')
        # attack_value = pokemons[pl1]['Moves'][move]* (1+(pokemons[pl1]['Stats']/100))

        attack(pl2, pl1)
        # print(f'{pl2} attacked with {move}')

        if pokemons[pl1]['Stats']['hp'] <= 0 or pokemons[pl2]['Stats']['hp'] <= 0:
            break
    print('Oh no, the pokemon can not fight any longer')

    if pokemons[pl1]['Stats']['hp'] <= 0:
        print(f'{pl1} has gone unconcious and {pl2} is the winner!!')
    else:
        print(f'{pl1} has gone unconcious and {pl2} is the winner!!')



