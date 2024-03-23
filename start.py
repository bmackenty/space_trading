# this is a text-based game where players are space traders
# and must travel between planets buying and selling goods
# to make a profit whilst avoiding dangers and managing their
# resources, diplomacy and relationships.


import random
# import sys
# import os
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
import player


playerOne = player.player("Player One")
print(playerOne.greet())
playerOne.setup()
print(playerOne.greet())

