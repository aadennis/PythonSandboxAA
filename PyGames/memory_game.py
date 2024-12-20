import pygame
import random
import time
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
PLACEHOLDER_HEIGHT = 100
PLACEHOLDER_WIDTH = 200

SHAPE_DISPLAY_TIME = 5  # seconds
DELAY_AFTER_SHAPE = 5  # seconds
DEFAULT_NUM_SHAPES = 4  # Default number of shapes to display (can be changed by user)

# Colors
BACKGROUND_COLOR = (255, 255, 255)
PLACEHOLDER_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Memory Game")

# Font for displaying text
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Load PNG images
shape_images = [
    pygame.image.load('shape1.png'),
    pygame.image.load('shape2.png'),
    pygame.image.load('shape3.png'),
    pygame.image.load('shape4.png'),
    pygame.image.load('shape5.png'),
    pygame.image.load('shape6.png'),
    pygame.image.load('shape7.png'),
    pygame.image.load('shape8.png')
]

# Function to get placeholder positions in an oval shape
def get_placeholder_positions_oval():
    positions = []
    center_x, center_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
    a, b = 300, 200  # horizontal and vertical radii of the oval
    for i in range(8):
        angle = math.pi / 4 * i  # angles equally spaced around the oval
        x = center_x + a * math.cos(angle) - PLACEHOLDER_HEIGHT // 2
        y = center_y + b * math.sin(angle) - PLACEHOLDER_WIDTH // 2
        positions.append((x, y))
    return positions

# Function to draw placeholders
def draw_placeholders(positions):
    for pos in positions:
        x, y = pos
        pygame.draw.rect(screen, PLACEHOLDER_COLOR, (x, y, PLACEHOLDER_WIDTH, PLACEHOLDER_HEIGHT))

# Function to display a shape
def display_shape(shape_idx, pos):
    x, y = pos
    shape_image = shape_images[shape_idx]
    screen.blit(shape_image, (x, y))

# Function to display the score
def display_score(score, num_shapes):
    screen.fill(BACKGROUND_COLOR)
    text = font.render(f'Your score is: {score} out of {num_shapes}', True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    # Display options to play again or quit
    play_again_text = small_font.render('Press P to Play Again or Q to Quit', True, TEXT_COLOR)
    play_again_rect = play_again_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
    screen.blit(play_again_text, play_again_rect)

    pygame.display.flip()

# Function to ask the user for the number of shapes
def ask_num_shapes():
    num_shapes = DEFAULT_NUM_SHAPES
    asking = True
    while asking:
        screen.fill(BACKGROUND_COLOR)
        question_text = small_font.render(f'The default number of shapes is {DEFAULT_NUM_SHAPES}.', True, TEXT_COLOR)
        question_rect = question_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100))
        screen.blit(question_text, question_rect)

        prompt_text = small_font.render('Enter a number between 2 and 8:', True, TEXT_COLOR)
        prompt_rect = prompt_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(prompt_text, prompt_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                asking = False
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if pygame.K_2 <= event.key <= pygame.K_8:
                    num_shapes = event.key - pygame.K_0
                    asking = False
                elif event.key == pygame.K_RETURN:
                    asking = False

    return num_shapes

# Function to run the game
def run_game():
    running = True
    while running:
        num_shapes = ask_num_shapes()
        if num_shapes is None:
            break

        score = 0
        placeholders = get_placeholder_positions_oval()
        screen.fill(BACKGROUND_COLOR)
        draw_placeholders(placeholders)
        pygame.display.flip()

        used_indices = []  # Track used shape indices to ensure uniqueness
        used_positions = []  # Track used placeholder positions to ensure uniqueness
        shapes_to_display = []
        for i in range(num_shapes):
            shape_idx = random.choice([idx for idx in range(len(shape_images)) if idx not in used_indices])
            used_indices.append(shape_idx)
            shape_pos = random.choice([pos for pos in placeholders if pos not in used_positions])
            used_positions.append(shape_pos)
            shapes_to_display.append((shape_idx, shape_pos))
            display_shape(shape_idx, shape_pos)
            pygame.display.flip()
            time.sleep(SHAPE_DISPLAY_TIME)
            screen.fill(BACKGROUND_COLOR)
            draw_placeholders(placeholders)

        # Wait for the configurable delay
        screen.fill(BACKGROUND_COLOR)
        draw_placeholders(placeholders)
        pygame.display.flip()
        time.sleep(DELAY_AFTER_SHAPE)

        # Randomize the sequence of shapes for user guesses
        random.shuffle(shapes_to_display)

        # User interaction loop
        for shape_idx, correct_pos in shapes_to_display:
            screen.fill(BACKGROUND_COLOR)
            draw_placeholders(placeholders)
            display_shape(shape_idx, (WINDOW_WIDTH // 2 - PLACEHOLDER_HEIGHT // 2, WINDOW_HEIGHT // 2 - PLACEHOLDER_HEIGHT // 2))
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
                            if x <= mouse_x <= x + PLACEHOLDER_WIDTH and y <= mouse_y <= y + PLACEHOLDER_HEIGHT:
                                guessed_pos = pos
                                break

            if guessed_pos == correct_pos:
                score += 1

        # Display the result and ask if the user wants to play again
        display_score(score, num_shapes)
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        waiting_for_input = False  # Restart the game
                    elif event.key == pygame.K_q:
                        running = False
                        waiting_for_input = False

    # Close Pygame
    pygame.quit()

# Main function
def main():
    run_game()

if __name__ == "__main__":
    main()