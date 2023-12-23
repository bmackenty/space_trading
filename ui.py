import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display with larger dimensions
width, height = 1024, 768  # Adjusted to make the window larger
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Roguelike Game Interface')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
GREEN = (0, 255, 0)

# Set up the font
font = pygame.font.Font(None, 24)

# Define column width, row height, and border thickness
column_width = 200
row_height = 100
border_thickness = 1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)




    # Draw left column with a green border
    left_column_border = pygame.Rect(0, 0, column_width, height - row_height)
    pygame.draw.rect(screen, GREEN, left_column_border, border_thickness)  # Here border_thickness is used
    left_column_inner = pygame.Rect(border_thickness, border_thickness,
                                    column_width - 2 * border_thickness, height - 2 * border_thickness - row_height)
    pygame.draw.rect(screen, BLACK, left_column_inner)

    # Draw right column with a green border
    right_column_border = pygame.Rect(width - column_width, 0, column_width, height - row_height)
    pygame.draw.rect(screen, GREEN, right_column_border, border_thickness)  # Here border_thickness is used
    right_column_inner = pygame.Rect(width - column_width + border_thickness, border_thickness,
                                    column_width - 2 * border_thickness, height - 2 * border_thickness - row_height)
    pygame.draw.rect(screen, BLACK, right_column_inner)

    # Draw bottom row with a green border
    bottom_row_border = pygame.Rect(0, height - row_height, width, row_height)  # Adjusted for the new width and height
    bottom_row_inner = pygame.Rect(border_thickness, height - row_height + border_thickness,
                                    width - 2 * border_thickness, row_height - 2 * border_thickness)
    pygame.draw.rect(screen, GREEN, bottom_row_border, border_thickness)
    pygame.draw.rect(screen, BLACK, bottom_row_inner)




    # Draw text for the left column
    left_text_surface = font.render('Left Column', True, WHITE)
    left_text_rect = left_text_surface.get_rect(center=(column_width // 2, (height - row_height) // 2))
    screen.blit(left_text_surface, left_text_rect)

    # Draw text for the right column
    right_text_surface = font.render('Right Column', True, WHITE)
    right_text_rect = right_text_surface.get_rect(center=(width - column_width // 2, (height - row_height) // 2))
    screen.blit(right_text_surface, right_text_rect)

    # Draw text for the bottom row
    bottom_text_surface = font.render('Bottom Row', True, WHITE)
    bottom_text_rect = bottom_text_surface.get_rect(center=(width // 2, height - row_height // 2))
    screen.blit(bottom_text_surface, bottom_text_rect)

    # Draw text for the middle section
    middle_text_surface = font.render('Middle Section', True, WHITE)
    middle_text_rect = middle_text_surface.get_rect(center=(width // 2, (height - row_height) // 2))
    screen.blit(middle_text_surface, middle_text_rect)


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()