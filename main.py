
from pokemons import pokemons
from asccii_pok import title
from clean_console import clear_console
from battleship import battle
from time import sleep


def game():
    print(title)
    print('Welcome to the amazing pokemon battle game!')
    while True:
        print('The pokemons willing to fight in this battle to defend your honor are: ')
        for n in pokemons:
            print("- " + n)
        print('Contestant 1, it is your turn.')
        while True:
            p1_choice= input('Choose a pokemon\n').title()
            if p1_choice in pokemons:
                print(f"Great choice! Your pokemon is {p1_choice}")
                break
            print('Sorry, that pokemon is recovering from a great battle today. Just Bulbasaur, Charmander or Squirtle are available')
        print('It is your turn player 2')
        while True:
            p2_choice = input('Choose a pokemon\n').title()
            if p2_choice == p1_choice:
                print("I know that pokemon is amazing, but it's been chosen by the contestant 1. Choose another one")
            elif p2_choice in pokemons:
                print(f"Great choice! Your pokemon is {p2_choice}")
                break
            else:
                print('Sorry, that pokemon is recovering from a great battle today. Just Bulbasaur, Charmander or Squirtle are available')
        sleep(2)
        clear_console()
        original_hp1= pokemons[p1_choice]['Stats']['hp']
        original_hp2= pokemons[p2_choice]['Stats']['hp']
        battle(p1_choice, p2_choice)
        pokemons[p1_choice]['Stats']['hp'] = original_hp1
        pokemons[p2_choice]['Stats']['hp'] = original_hp2

        restart = input('Do you want to play again (y/n):').lower()
        if restart != 'y':
            break
    print('Thanks for playing. See you next time')
    sleep(2)
    clear_console()

    print(title)
    sleep(1)





game()
