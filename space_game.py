# this is a text-based game where players are space traders
# and must travel between planets buying and selling goods
# to make a profit. 



# import modules
import display_menu
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
# import player

# some functions
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Space Trader!")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Help")
    print("4. Settings")
    print("5. Credits")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new_game()
    elif choice == "2":
        load_game()
    elif choice == "3":
        help()
    elif choice == "4":
        settings()
    elif choice == "5":
        credits()
    elif choice == "6":
        sys.exit()
    else:
        print("Invalid choice. Try again.")
        display_menu()



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

# def game_loop():
    # game loop
    # while True:
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
        # display_menu()
        # pass

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