import os
import pygame

# Set my basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

# Initialize pygame
HEIGHT = 600
WIDTH = 700
FPS = 30  # Frames per second
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
pygame.init()  # Turns on pygame
pygame.font.init() # Allows us to set a font type for words on the screen
pygame.mixer.init()  # Turns on sound in pygame
sound1 = pygame.mixer.Sound('blip.wav')
sound2 = pygame.mixer.Sound('blip2.wav')
font_name = pygame.font.match_font('Times New Roman')
font = pygame.font.Font(font_name, 30)
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,200'   # Sets where your game window appears on the screen
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BLACK)
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# We need 2 paddles, 1 ball, and a score
# Paddle A
pad_a_x = 15
pad_a_y = 250
# Paddle B
pad_b_x = 675
pad_b_y = 250
# Ball
ball_x = 350
ball_y = 300
ball_radius = 10
move_x = 5
move_y = 5
# Score
score_a = 0
score_b = 0

# Draw Screen
def draw_screen():
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, (pad_a_x, pad_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, WHITE, (pad_b_x, pad_b_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)
    text = "Player A:  {}  Player B:  {}".format(score_a, score_b)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(midtop=(WIDTH//2, 15))
    window.blit(text_surface, text_rect)
    pygame.display.update()


playing = True
while playing:
    clock.tick(FPS)
    draw_screen()
    global event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Move the paddles
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if pad_b_y > 0:
                pad_b_y -= 20
        elif event.key == pygame.K_DOWN:
            if pad_b_y < 500:
                pad_b_y += 20
        elif event.key == pygame.K_a:
            if pad_a_y > 0:
                pad_a_y -= 20
        elif event.key == pygame.K_z:
            if pad_a_y < 500:
                pad_a_y += 20

    # Move the ball
    ball_x += move_x
    ball_y += move_y
    # Check if ball hits top or bottom
    if ball_y < 10 or ball_y > 590:
        move_y *= -1
        sound1.play()
    # Check if ball goes out of bounds
    if ball_x > 700:
        ball_x = 350
        ball_y = 300
        score_a += 1
        sound2.play()
    if ball_x < 0:
        ball_x = 350
        ball_y = 300
        score_b += 1
        sound2.play()
    # Check if ball hits a paddle
    if (ball_x <= 35) and (ball_y + 10) in range(pad_a_y, pad_a_y+100):
        move_x *= -1
        sound1.play()
    if (ball_x + 10) >= 675 and (ball_y + 10) in range(pad_b_y, pad_b_y+100):
        move_x *= -1
        sound1.play()

