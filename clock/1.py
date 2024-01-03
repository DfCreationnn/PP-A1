import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CLOCK_RADIUS = 150
CENTER = (WIDTH // 2, HEIGHT // 2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")

def draw_clock():
    pygame.draw.circle(screen, BLACK, CENTER, CLOCK_RADIUS, 2)  # Clock outline

    # Draw hour marks
    for i in range(12):
        angle = math.radians(i * 30)
        x = int(CENTER[0] + (CLOCK_RADIUS - 10) * math.cos(angle))
        y = int(CENTER[1] + (CLOCK_RADIUS - 10) * math.sin(angle))
        pygame.draw.circle(screen, BLACK, (x, y), 5)

    # Get current time
    current_time = datetime.now().time()
    hours, minutes, seconds = current_time.hour % 12, current_time.minute, current_time.second

    # Draw hour hand
    hour_angle = math.radians((hours % 12) * 30 - 90)
    hour_hand_length = CLOCK_RADIUS - 50
    hour_hand_end = (int(CENTER[0] + hour_hand_length * math.cos(hour_angle)),
                     int(CENTER[1] + hour_hand_length * math.sin(hour_angle)))
    pygame.draw.line(screen, BLACK, CENTER, hour_hand_end, 8)

    # Draw minute hand
    minute_angle = math.radians(minutes * 6 - 90)
    minute_hand_length = CLOCK_RADIUS - 30
    minute_hand_end = (int(CENTER[0] + minute_hand_length * math.cos(minute_angle)),
                       int(CENTER[1] + minute_hand_length * math.sin(minute_angle)))
    pygame.draw.line(screen, BLACK, CENTER, minute_hand_end, 4)

    # Draw second hand
    second_angle = math.radians(seconds * 6 - 90)
    second_hand_length = CLOCK_RADIUS - 20
    second_hand_end = (int(CENTER[0] + second_hand_length * math.cos(second_angle)),
                       int(CENTER[1] + second_hand_length * math.sin(second_angle)))
    pygame.draw.line(screen, BLACK, CENTER, second_hand_end, 2)

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)  # White background
    draw_clock()

    pygame.display.flip()
    clock.tick(20)  # Update once per second
