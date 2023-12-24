import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1024, 768
BLACK, WHITE, GREY, GREEN = (0, 0, 0), (255, 255, 255), (192, 192, 192), (0, 255, 0)
COLUMN_WIDTH, ROW_HEIGHT, BORDER_THICKNESS = 200, 100, 1
LEFT_COLUMN_TEXT, RIGHT_COLUMN_TEXT, BOTTOM_ROW_TEXT, MIDDLE_SECTION_TEXT = 'Left Column', 'Right Column', 'Bottom Row', 'Middle Section'

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Roguelike Game Interface')

# Set up the font
try:
    font = pygame.font.Font(None, 24)
except IOError:
    print("Font not found! Using default font.")
    font = pygame.font.SysFont(None, 24)

# Function to draw bordered box
def draw_bordered_box(x, y, width, height, border_color, inner_color, border_thickness):
    pygame.draw.rect(screen, border_color, (x, y, width, height), border_thickness)
    inner_rect = (x + border_thickness, y + border_thickness,
                  width - 2 * border_thickness, height - 2 * border_thickness)
    pygame.draw.rect(screen, inner_color, inner_rect)

# Function to draw text
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw columns and rows
    draw_bordered_box(0, 0, COLUMN_WIDTH, HEIGHT - ROW_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)
    draw_bordered_box(WIDTH - COLUMN_WIDTH, 0, COLUMN_WIDTH, HEIGHT - ROW_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)
    draw_bordered_box(0, HEIGHT - ROW_HEIGHT, WIDTH, ROW_HEIGHT, GREEN, BLACK, BORDER_THICKNESS)

    # Draw text
    draw_text(LEFT_COLUMN_TEXT, COLUMN_WIDTH // 2, (HEIGHT - ROW_HEIGHT) // 2)
    draw_text(RIGHT_COLUMN_TEXT, WIDTH - COLUMN_WIDTH // 2, (HEIGHT - ROW_HEIGHT) // 2)
    draw_text(BOTTOM_ROW_TEXT, WIDTH // 2, HEIGHT - ROW_HEIGHT // 2)
    draw_text(MIDDLE_SECTION_TEXT, WIDTH // 2, (HEIGHT - ROW_HEIGHT) // 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
