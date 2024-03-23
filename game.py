# game.py
import pygame

class Game:
    def __init__(self):
        # Initialize any necessary game state here
        self.some_state = "Initial State"

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
        # Update game state if necessary
        pass

    def draw(self, screen):
        # Update the display based on the current game state
        # This function needs a reference to the Pygame screen to draw on
        pass
