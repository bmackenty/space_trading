# this is a text-based game where players are space traders
# and must travel between planets buying and selling goods
# to make a profit. 

# there are pirates
# players can build a ships, and upgrade the ship
# players can buy and sell goods
# players can buy and sell fuel
# players can buy and sell ships
# players can buy and sell upgrades
# players can buy and sell planets
# players can buy and sell space stations
# players can build bases


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
# import aliens
import missions
import events
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



os.system('cls' if os.name == 'nt' else 'clear')



print("There are " + str(len(planets.planets)) + " planets in this universe.")
print("There are " + str(len(goods.goods)) + " goods in this universe.")
print("There are " + str(len(ships.ship_classes)) + " ship types in this universe.")
print("There are " + str(len(stations.space_stations)) + " space station types in this universe.")
print("There are " + str(len(markets.markets)) + " markets in this universe.")
print("There are " + str(len(factories.factories)) + " factories in this universe.")
print("There are " + str(len(pirates.pirates)) + " pirate in this universe.")
print("There are " + str(len(organizations.organizations)) + " organizations in this universe.")
print("There are " + str(len(missions.missions)) + " missions in this universe.")