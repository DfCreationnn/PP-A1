import pygame
from random import randrange as r
import sys

# Initialize Pygame
pygame.init()

class Variables:
    def __init__(self):
        self.note = "Note that when the program has finished, it will say: 'Process finished with exit code 0'"
        self.User_input = ""
        self.after = "The number you chose is perfect"
        self.User_int = 0
        self.error = "Error, please choose another number"
        self.start_signal = 0
        self.random_number_chooser = r(1, 1000000)
        self.random_number = r(1, self.random_number_chooser)
        self.load1 = 0
        self.load2 = 0
        self.load_p = 0
        self.load_p_adder = 5.546248245
        self.load_pstr = str(self.load_p)
        self.done1 = "Done!"
        self.counter = 0
        self.counter_str = str(self.counter)
        self.end1 = f"The number you chose matched the number that the program chose in {self.counter_str} tries"
        self.error404 = "Error 404, number input not found"
        self.error4040 = 0
        self.lucky = 0
        self.lucky_sms = "You are lucky, so you got -1000 from the score!!!!!!"

    def get_user_input(self):
        # Pygame event loop to get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    self.User_input = self.User_input[:-1]
                elif event.unicode.isdigit():
                    self.User_input += event.unicode
        return False

    def generate_lucky_number(self):
        self.lucky = r(0, 20)

# Pygame initialization
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Example usage:
if __name__ == "__main__":
    variables_instance = Variables()
    variables_instance.generate_lucky_number()

    while True:
        # Pygame event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get user input
        input_done = variables_instance.get_user_input()

        # Display information on the Pygame window
        screen.fill((255, 255, 255))  # White background
        font = pygame.font.Font(None, 36)
        text = font.render(variables_instance.User_input, True, (0, 0, 0))
        screen.blit(text, (10, 10))
        pygame.display.flip()

        if input_done:
            variables_instance.User_int = int(variables_instance.User_input)
            # Rest of your program...
            print(f"You entered: {variables_instance.User_int}")

    pygame.quit()
