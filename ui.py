import pygame
import sys
import time
from game import Game 


# Initialize Pygame
pygame.init()
game = Game()

# Constants
WIDTH, HEIGHT = 1024, 768
BLACK, WHITE, GREY, GREEN = (0, 0, 0), (255, 255, 255), (192, 192, 192), (0, 255, 0)
COLUMN_WIDTH, ROW_HEIGHT, BORDER_THICKNESS = 200, 100, 1
HEADER_HEIGHT = 50  # Height of the header
HEADER_TEXT = 'Space Trading Game'  # Text to display in the header
LEFT_COLUMN_TEXT, RIGHT_COLUMN_TEXT, BOTTOM_ROW_TEXT, MIDDLE_SECTION_TEXT = 'Left Column', 'Right Column', 'Bottom Row', 'Middle Section'

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Trading Game')

# Set up the font
try:
    font = pygame.font.Font(None, 14)
except IOError:
    print("Font not found! Using default font.")
    font = pygame.font.SysFont(None, 24)

# Function to draw bordered box
def draw_bordered_box(x, y, width, height, border_color, inner_color, border_thickness, draw_top_bottom=True):
    if draw_top_bottom:
        pygame.draw.rect(screen, border_color, (x, y, width, height), border_thickness)
    else:
        # Draw only side borders
        pygame.draw.line(screen, border_color, (x, y), (x, y + height), border_thickness)  # Left border
        pygame.draw.line(screen, border_color, (x + width - border_thickness, y), (x + width - border_thickness, y + height), border_thickness)  # Right border

    inner_rect = (x + border_thickness, y + border_thickness,
                  width - 2 * border_thickness, height - 2 * border_thickness)
    pygame.draw.rect(screen, inner_color, inner_rect)

# Function to draw text
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to update text
def update_text():
    global LEFT_COLUMN_TEXT, RIGHT_COLUMN_TEXT, BOTTOM_ROW_TEXT, MIDDLE_SECTION_TEXT
    # Example of dynamic text update
    LEFT_COLUMN_TEXT = 'Updated Left Column'
    RIGHT_COLUMN_TEXT = 'Updated Right Column'
    BOTTOM_ROW_TEXT = 'Updated Bottom Row'
    MIDDLE_SECTION_TEXT = 'Updated Middle Section'


 # Variables for timing text updates
last_update_time = time.time()
update_interval = 5  # update every 5 seconds


# Function to draw header
def draw_header():
    draw_bordered_box(0, 0, WIDTH, HEADER_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)
    draw_text(HEADER_TEXT, WIDTH // 2, HEADER_HEIGHT // 2)

# Game loop
running = True
while running:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game.handle_event(event)  # Pass the event to the game for processing
    
    game.update()


    # # Update text periodically
    # if current_time - last_update_time > update_interval:
    #     update_text()
    #     last_update_time = current_time

    screen.fill(BLACK)

    # Draw header
    draw_header()

    # Draw columns and rows with adjusted borders
    draw_bordered_box(0, HEADER_HEIGHT, COLUMN_WIDTH, HEIGHT - ROW_HEIGHT - HEADER_HEIGHT, GREEN, BLACK, BORDER_THICKNESS, draw_top_bottom=False)
    draw_bordered_box(WIDTH - COLUMN_WIDTH, HEADER_HEIGHT, COLUMN_WIDTH, HEIGHT - ROW_HEIGHT - HEADER_HEIGHT, GREEN, BLACK, BORDER_THICKNESS, draw_top_bottom=False)
    draw_bordered_box(0, HEIGHT - ROW_HEIGHT, WIDTH, ROW_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)

    # Draw text
    draw_text(LEFT_COLUMN_TEXT, COLUMN_WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2)
    draw_text(RIGHT_COLUMN_TEXT, WIDTH - COLUMN_WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2)
    draw_text(BOTTOM_ROW_TEXT, WIDTH // 2, HEIGHT - ROW_HEIGHT // 2)
    draw_text(MIDDLE_SECTION_TEXT, WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2)

    pygame.display.flip()

   

pygame.quit()
sys.exit()
