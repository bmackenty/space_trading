import pygame
import time
from game import Game 
from ui_character_sheet import draw_character_sheet

# Initialize Pygame
pygame.init()


# Constants
WIDTH, HEIGHT = 1024, 768
BLACK, WHITE, GREY, GREEN = (0, 0, 0), (255, 255, 255), (192, 192, 192), (0, 255, 0)
COLUMN_WIDTH, ROW_HEIGHT, BORDER_THICKNESS = 200, 100, 1
HEADER_HEIGHT = 50  # Height of the header

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Trading Game')

# Initialize the game
game = Game(screen)

# text:
HEADER_TEXT = game.header_text
LEFT_COLUMN_TEXT = game.left_column_text
RIGHT_COLUMN_TEXT = game.right_column_text
BOTTOM_ROW_TEXT = game.bottom_row_text
MIDDLE_SECTION_TEXT = game.middle_section_text


# Set up the font
try:
    font = pygame.font.Font(None, 18)
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


def draw_multiline_text(surface, text, pos):
    """
    Draws multi-line text on the given surface.
    
    Parameters:
    - surface: Pygame surface to draw text on.
    - text: The multi-line text string to be drawn.
    - pos: A tuple (x, y) representing the top-left corner from where text rendering will start.
    """
    lines = text.split('\n')
    x, y = pos
    for line in lines:
        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)
        # Move to the next line by adjusting the y-coordinate; adjust the value for different spacing
        y += font.get_linesize()  # or use a fixed value like font.get_height() + 2


# Function to draw header
def draw_header():
    draw_bordered_box(0, 0, WIDTH, HEADER_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)
    draw_text(HEADER_TEXT, WIDTH // 2, HEADER_HEIGHT // 2)

# function to draw column
def draw_columns():
    draw_bordered_box(0, HEADER_HEIGHT, COLUMN_WIDTH, HEIGHT - ROW_HEIGHT - HEADER_HEIGHT, GREEN, BLACK, BORDER_THICKNESS, draw_top_bottom=False)
    draw_bordered_box(WIDTH - COLUMN_WIDTH, HEADER_HEIGHT, COLUMN_WIDTH, HEIGHT - ROW_HEIGHT - HEADER_HEIGHT, GREEN, BLACK, BORDER_THICKNESS, draw_top_bottom=False)
    draw_bordered_box(0, HEIGHT - ROW_HEIGHT, WIDTH, ROW_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)

def write_text_to_display():
    # draw_text(LEFT_COLUMN_TEXT, COLUMN_WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2)
    draw_multiline_text(screen, LEFT_COLUMN_TEXT, (COLUMN_WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2))
    draw_text(RIGHT_COLUMN_TEXT, WIDTH - COLUMN_WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2)
    draw_text(BOTTOM_ROW_TEXT, WIDTH // 2, HEIGHT - ROW_HEIGHT // 2)
    draw_text(MIDDLE_SECTION_TEXT, WIDTH // 2, HEADER_HEIGHT + (HEIGHT - ROW_HEIGHT - HEADER_HEIGHT) // 2)

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
    screen.fill(BLACK)

    # Draw ui
    draw_header()
    draw_columns()
    write_text_to_display()

    pygame.display.flip()

pygame.quit()

