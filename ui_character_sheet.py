import pygame

def draw_character_sheet(screen, font):
    # Constants for the character sheet
    sheet_width, sheet_height = 600, 400
    start_x, start_y = (screen.get_width() - sheet_width) // 2, (screen.get_height() - sheet_height) // 2
    sheet_color = (50, 50, 50)  # Dark grey

    # Draw the character sheet background
    pygame.draw.rect(screen, sheet_color, (start_x, start_y, sheet_width, sheet_height))

    # Example text to display on the character sheet
    text = "Character Sheet\n\nName: John Doe\nLevel: 5\nClass: Wizard"
    draw_multiline_text(screen, font, text, (start_x + 20, start_y + 20))

def draw_multiline_text(screen, font, text, pos):
    lines = text.split('\n')
    x, y = pos
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))  # White color for text
        screen.blit(text_surface, (x, y))
        y += font.get_height() + 2  # Move to the next line
