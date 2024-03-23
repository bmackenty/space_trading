# game.py
import pygame

class Game:
    def __init__(self, screen):
        # Initialize any necessary game state here
        self.some_state = "Initial State"
        self.screen = screen

        #initial text
        self.header_text = "Space Trading Game!!"
        self.left_column_text = "player information"
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
