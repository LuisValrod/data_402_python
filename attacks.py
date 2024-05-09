from pokemons import pokemons
from clean_console import clear_console
import time

def attack(attck, defend):
    print(f"It is your turn {attck}. Chose one of these attacks:")
    for n in pokemons[attck]['Moves']:
        print(f"- {n}")
    while True:
        move = input('Choose your attack: ').title()
        if move in pokemons[attck]['Moves']:
            break
        print('Sorry, make sure you are choosing an available attack')
    clear_console()
    print(f'{attck} attacked with {move}')
    attack_value = pokemons[attck]['Moves'][move] * (1 + (pokemons[attck]['Stats']['attack'] / 100))
    if attack_value > 0:
        attack_value -= ((pokemons[defend]['Stats']['defense']/150) * pokemons[attck]['Stats']['attack'])
    if (pokemons[defend]['Stats']['type'] == 'plant' and pokemons[attck]['Stats']['type'] == 'fire') or (pokemons[defend]['Stats']['type'] == 'fire' and pokemons[attck]['Stats']['type'] == 'water') or (pokemons[defend]['Stats']['type'] == 'water' and pokemons[attck]['Stats']['type'] == 'plant'):
        print(f'Oh no, {defend} is weak against pokemons of {pokemons[attck]['Stats']['type']}')
        attack_value *= 1.4
    hp_points = round(attack_value)
    print(f'{defend} has lost {hp_points} hp points')
    time.sleep(1)
    pokemons[defend]['Stats']['hp'] -= hp_points
    print(f'{defend} has {pokemons[defend]['Stats']['hp']} health points remaining')
