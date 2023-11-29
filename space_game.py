# this is a text-based game where players are space traders
# and must travel between planets buying and selling goods
# to make a profit. 



# import modules
import random
import sys
import os
import goods
import planets
import ships
import stations
# import bases
import markets
import factories
import pirates
import organizations
import races
import missions
import events
# import space
# import combat
# import diplomacy
# import trade
# import travel
# import save
# import load
# import help
# import settings
# import credits
from player import *

# some functions
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Space Trader!")
    print("1. Create new character")
    print("2. Start new game")
    print("3. Load Game")
    print("4. Help")
    print("5. Settings")
    print("6. Credits")
    print("7. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new_character()
    elif choice == "2":
        new_game()
    elif choice == "3":
        load_game()
    elif choice == "4":
        help()
    elif choice == "5":
        settings()
    elif choice == "6":
        credits()
    elif choice == "7":
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        display_menu()

def new_character():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Generating new character...")
    current_player = Player_stats("Boris")
    Player_stats.greet(current_player)
    press_enter = input("Press enter to continue.")
    return current_player
    
def new_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting new game...")
    press_enter = input("Press enter to continue.")
    print("=" * 80)
    print("Welcome to Space Trader!")
    print("=" * 80)
    print()
    print()
    print("Name: " + current_player.name)

    press_enter = input("Press enter to continue.")






# print("There are " + str(len(planets.planets)) + " planets in this universe.")
# print("There are " + str(len(goods.goods)) + " goods in this universe.")
# print("There are " + str(len(goods.good_categories)) + " good categories in this universe.")
# print("There are " + str(len(ships.ship_classes)) + " ship types in this universe.")
# print("There are " + str(len(ships.ship_upgrades)) + " ship upgrades in this universe.")
# print("There are " + str(len(stations.space_stations)) + " space station types in this universe.")
# print("There are " + str(len(markets.markets)) + " markets in this universe.")
# print("There are " + str(len(factories.factories)) + " factories in this universe.")
# print("There are " + str(len(pirates.pirates)) + " pirates in this universe.")
# print("There are " + str(len(organizations.organizations)) + " organizations in this universe.")
# print("There are " + str(len(missions.missions)) + " missions in this universe.")
# print("There are " + str(len(events.random_events)) + " events in this universe.")
# print("There are " + str(len(races.races)) + " races in this universe.")


def game_loop():
    # game loop
    while True:
        # update_space()
        # update_combat()
        # update_diplomacy()
        # update_trade()
        # update_travel()
        # update_economy()
        # update_politics()
        # update_missions()
        # update_events()
        # update_factories()
        # update_pirates()
        # update save()
        # update_player()
        display_menu()
        pass


# start the game
game_loop()