import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
PLACEHOLDER_SIZE = 100
SHAPE_DISPLAY_TIME = 5  # seconds
DELAY_AFTER_SHAPE = 5  # seconds

# Colors
BACKGROUND_COLOR = (255, 255, 255)
PLACEHOLDER_COLOR = (200, 200, 200)
SHAPE_COLOR_1 = (255, 0, 0)
SHAPE_COLOR_2 = (0, 0, 255)
TEXT_COLOR = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Game")

# Font for displaying text
font = pygame.font.Font(None, 74)

# Function to draw placeholders
def draw_placeholders():
    positions = []
    for i in range(4):
        for j in range(2):
            x = (WINDOW_WIDTH // 4) * i + (WINDOW_WIDTH // 8) - (PLACEHOLDER_SIZE // 2)
            y = (WINDOW_HEIGHT // 2) * j + (WINDOW_HEIGHT // 4) - (PLACEHOLDER_SIZE // 2)
            positions.append((x, y))
            pygame.draw.rect(screen, PLACEHOLDER_COLOR, (x, y, PLACEHOLDER_SIZE, PLACEHOLDER_SIZE))
    return positions

# Function to display a shape
def display_shape(shape, pos):
    x, y = pos
    if shape == 1:
        # Draw a complex shape for shape 1
        pygame.draw.polygon(screen, SHAPE_COLOR_1, [
            (x + 20, y), (x + 80, y), (x + 100, y + 20), (x + 100, y + 80), (x + 80, y + 100), (x + 20, y + 100), (x, y + 80), (x, y + 20)
        ])
    elif shape == 2:
        # Draw a complex shape for shape 2
        pygame.draw.polygon(screen, SHAPE_COLOR_2, [
            (x + 50, y), (x + 70, y + 30), (x + 100, y + 30), (x + 80, y + 50), (x + 90, y + 80), (x + 50, y + 60), (x + 10, y + 80), (x + 20, y + 50), (x, y + 30), (x + 30, y + 30)
        ])

# Function to display the score
def display_score(score):
    screen.fill(BACKGROUND_COLOR)
    text = font.render(f'Your score is: {score} out of 2', True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(3)  # Display the score for 3 seconds

# Main game loop
def main():
    running = True
    score = 0
    placeholders = draw_placeholders()
    pygame.display.flip()

    # Display the first shape
    shape1_pos = random.choice(placeholders)
    display_shape(1, shape1_pos)
    pygame.display.flip()
    time.sleep(SHAPE_DISPLAY_TIME)

    # Display the second shape
    screen.fill(BACKGROUND_COLOR)
    draw_placeholders()
    shape2_pos = random.choice(placeholders)
    display_shape(2, shape2_pos)
    pygame.display.flip()
    time.sleep(SHAPE_DISPLAY_TIME)

    # Wait for the configurable delay
    screen.fill(BACKGROUND_COLOR)
    draw_placeholders()
    pygame.display.flip()
    time.sleep(DELAY_AFTER_SHAPE)

    # Randomize the sequence of shapes for user guesses
    shapes_to_guess = [(1, shape1_pos), (2, shape2_pos)]
    random.shuffle(shapes_to_guess)

    # User interaction loop
    for shape, correct_pos in shapes_to_guess:
        screen.fill(BACKGROUND_COLOR)
        draw_placeholders()
        display_shape(shape, (WINDOW_WIDTH // 2 - PLACEHOLDER_SIZE // 2, WINDOW_HEIGHT // 2 - PLACEHOLDER_SIZE // 2))
        pygame.display.flip()
        guessed_pos = None

        while guessed_pos is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    guessed_pos = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for pos in placeholders:
                        x, y = pos
                        if x <= mouse_x <= x + PLACEHOLDER_SIZE and y <= mouse_y <= y + PLACEHOLDER_SIZE:
                            guessed_pos = pos
                            break

        if guessed_pos == correct_pos:
            score += 1

    # Display the result
    display_score(score)

    # Close Pygame
    pygame.quit()

if __name__ == "__main__":
    main()