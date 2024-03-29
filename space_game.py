# this is a text-based game where players are space traders
# and must travel between planets buying and selling goods
# to make a profit whilst avoiding dangers and managing their
# resources, diplomacy and relationships.


import random
# import sys
# import os
import goods
import planets
# import ships
# import stations
# import bases
import markets
# import factories
# import pirates
import organizations
# import races
# import missions
# import events
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
# from player import *

# some classes

class Player:
    def __init__(self, name):
        self.name = name
        self.ship = Ship("Starter Ship", capacity=100, speed=10, health=100, ship_type="Cargo")
        self.id = None
        self.money = 1000
        self.ship = None
        self.cargo = []
        self.weapons = []
        self.upgrades = []
        self.faction = None
        self.reputation = 0
        self.skills = {}
        self.missions = []
        self.location = None
        self.traveling = False
        self.health = 100
        self.energy = 100
        self.race = None
        self.crew = []
        self.affiliations = []

    @classmethod
    def create_new_player(cls, name):
        return cls(name)

    def update_player(self, **updates):
        for attribute, value in updates.items():
            if hasattr(self, attribute):
                setattr(self, attribute, value)


    # Update player's money
    def add_money(self, amount):
        self.money += amount

    # Assign a new mission
    def assign_mission(self, mission):
        self.missions.append(mission)

    # Print player stats
    def display_stats(self):
        print(f"Player: {self.name}")
        print(f"Money: {self.money}")
        print(f"Health: {self.health}")
        print(f"Reputation: {self.reputation}")

        
    def check_ship_cargo(self):
        if self.ship:
            self.ship.display_cargo()
        else:
            print("You do not have a ship.")

class Ship:
    def __init__(self, name, ship_type, capacity, speed, health, weapons=[], upgrades=[]):
        self.name = name
        self.capacity = capacity  # Max cargo the ship can hold
        self.speed = speed        # Determines how fast the ship can travel
        self.health = health      # Ship's health points
        self.weapons = weapons    # List of weapons the ship has
        self.upgrades = upgrades  # Ship upgrades like shields, engines, etc.
        self.cargo = []           # Current cargo of the ship
        self.ship_type = None     # Type of ship, e.g. Cargo, Fighter, etc.
        self.crew = []            # List of crew members on the ship
        self.fuel = 100           # Fuel level of the ship
        self.location = None      # Current location of the ship
        self.destination = None   # Destination of the ship
        self.traveling = False    # Whether the ship is traveling or not
        self.docked = False       # Whether the ship is docked or not
        self.ai_level = 0         # AI level of the ship
        self.stealth = 0          # Stealth level of the ship
        self.sensor = 0           # Sensor level of the ship
        self.comms = 0            # Communication level of the ship
        self.armor = 0            # Armor level of the ship
        self.shields = 0          # Shield level of the ship
        self.manufacturers = []   # List of manufacturers of the ship
        self.tech_level = 0       # Tech level of the ship
        self.condition = None     # Condition of the ship
        

    def add_cargo(self, item):
        if len(self.cargo) < self.capacity:
            self.cargo.append(item)
        else:
            print("Cargo hold is full!")



    def remove_cargo(self, item):
        if item in self.cargo:
            self.cargo.remove(item)
        else:
            print("Item not in cargo!")

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            print("Ship is destroyed!")

    def has_cargo(self):
        return bool(self.cargo)

    def display_cargo(self):
        if self.cargo:
            print(f"{self.name} Cargo:")
            for item in self.cargo:
                print(f"- {item}")
        else:
            print("Cargo hold is empty.")

    # You can add more methods related to ship functionality like repair, upgrade, travel, etc.

class Planet:
    def __init__(self, name,market, location,type,size,population,government_type,economic_status,technological_level,resource_abundance,cultural_characteristics,stability,climate,strategic_importance,trade_regulations,black_market_activity,spaceport_facilities,alliances_and_conflicts,historical_significance,orbital_position,special_conditions,local_customs):
        self.name=name
        self.type=type
        self.market = market
        self.size=0
        self.population=0
        self.government_type=None
        self.economic_status=None
        self.technological_level=0
        self.resource_abundance=0
        self.cultural_characteristics=None
        self.stability=0 
        self.climate=0
        self.strategic_importance=0 
        self.trade_regulations=None 
        self.black_market_activity=0 
        self.spaceport_facilities=0 
        self.alliances_and_conflicts=None
        self.historical_significance=0 
        self.orbital_position=0 
        self.special_conditions=None 
        self.local_customs=None
        self.location = location

    def display_market_info(self):
        if self.market:
            print(f"Market on {self.name}: {self.market['Name']}")
            for key, value in self.market.items():
                print(f"{key}: {value}")
        else:
            print("No market on this planet.")

class GameState:
    def __init__(self):
        self.player = None
        # You can add more attributes here as needed, like:
        # self.current_planet = None
        self.game_turn = 0
        # self.global_events = []
        self.planets = {}  # To store planet objects


    def set_player(self, player):
        self.player = player

    def update_game_state(self):
        self.game_turn += 1
        # Update game state here

    def display_game_state(self):
        print(f"Game Turn: {self.game_turn}")
        print(f"Player: {self.player.name}")
        print(f"Ship: {self.player.ship.name}")

        #randomly select a planet:
        planet = random.choice(list(self.planets.values()))
        print(f"Planet: {planet.name}")
        print(f"Market: {planet.market['Name']}")
        print(f"Location: {planet.location}")
        
        #randomly select a good category:
        good_category = random.choice(list(goods.good_categories.keys()))
        print(f"Good Category: {good_category}") 

        #randomly select an organization:
        organization = random.choice(list(organizations.organizations.keys()))
        print(f"Organization: {organization}")

        pass

    def load_planets(self, planets_data, markets_data):
        for name, attributes in planets_data.items():
            market_name = random.choice(list(markets_data.keys()))
            market = markets_data[market_name]
            self.planets[name] = Planet(**attributes, market=market)

    # Additional methods to manage game state can be added here
    # Such as methods to change the current planet, update global events, etc.

class Main:
    def __init__(self):
        self.game_state = GameState()
        self.running = True

    def start_game(self):
        # This method could include any initialization logic before the game loop starts
        print("Welcome to Space Trader!")
        # For example, creating a new player or loading game data
        self.game_state.set_player(Player.create_new_player("Commander Shepard"))
        # new ship:
        self.game_state.player.ship = Ship("Starter Ship", capacity=100, speed=10, health=100, ship_type="Cargo")
        # load planets:
        self.game_state.load_planets(planets.planets_data, markets.markets_data)  # Assuming planets_data is in planets.py


    def game_loop(self):
        while self.running:
            self.display_menu()
            self.process_input()

    def display_menu(self):
        # Display the main menu or game options
        print("1. New Game")
        print("2. Load Game")
        print("3. Show player stats")
        print("4. Increment game state")
        print("5. Check ship cargo")
        print("6. Show planets")
        print("7. Exit")
        # Add more menu options as necessary

    def process_input(self):
        choice = input("Enter your choice: ")
        if choice == "1":
            self.start_new_game()
        elif choice == "2":
            self.load_game()
        elif choice == "3":
            self.game_state.player.display_stats()
        
        elif choice == "4":
            self.game_state.update_game_state()
            self.game_state.display_game_state()
        elif choice == "5":
            self.game_state.player.check_ship_cargo()
        elif choice == "6":
            for planet in self.game_state.planets.values():
                print(planet.name)
                print(planet.location)
                
          


        elif choice == "7":
            self.exit_game()
        else:
            print("Invalid choice. Please try again.")

    def start_new_game(self):
        # Logic to start a new game
        print("Starting new game...")
        # Potentially call methods from game_state to set up the new game

    def load_game(self):
        # Logic to load a saved game
        print("Loading game...")
        # Implement game loading functionality

    def exit_game(self):
        print("Exiting game. Thank you for playing!")
        self.running = False

# Main execution
if __name__ == "__main__":
    game = Main()
    game.start_game()
    game.game_state.load_planets(planets.planets_data, markets.markets_data)
    game.game_loop()