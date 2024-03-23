# game.py

# this is a text-based game where players are space traders
# and must travel between planets buying and selling goods
# to make a profit whilst avoiding dangers and managing their
# resources, diplomacy and relationships.


import random
import pygame
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

class Game:
    def __init__(self, screen):
        # Initialize any necessary game state here
        self.some_state = "Initial State"
        self.screen = screen
        playerOne = player.player("Player One")

        #initial text
        self.header_text = "Space Trading Game!!"
        # provide player information below: 
        player_info = playerOne.greet()
        self.left_column_text = player_info
        self.right_column_text = "mission / cargo / ship information"
        self.bottom_row_text = "game status, turn, etc.."
        self.middle_section_text = "market / planet / station information"

    def handle_event(self, event):
        # This method processes a single event
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse click
            self.some_state = f"Mouse clicked at {event.pos}"
            print(self.some_state)
        elif event.type == pygame.KEYDOWN:
            # Handle key press
            if event.key == pygame.K_SPACE:
                self.some_state = "Spacebar pressed"
                print(self.some_state)
        

    def update(self):
        # Update game state
        pass

    def draw(self):
        pass
