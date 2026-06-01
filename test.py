import pygame
from buttons import Button
from text_input import Text
from state_handeling import States

pygame.init()

# -------------------------
# Setup
# -------------------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UI Tutorial Test")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# -------------------------
# Create UI Elements - Buttons
# -------------------------
states = States("start")  # Create state manager with default state "start"

# See buttons.py for how to create buttons wiht .png files
red_btn = Button.create_colored_button(100, 350, (200, 50, 50), "Red")  # Create red button at x=100, y=350
orange_btn = Button.create_colored_button(325, 350, (255, 140, 0), "Orange")  # Create orange button at x=325, y=350
blue_btn = Button.create_colored_button(550, 350, (50, 100, 255), "Blue")  # Create blue button at x=550, y=350

# -------------------------
# Create UI Elements - Text Inputs
# -------------------------
text_box = Text.create_text_input(300, 150, font, mode="text")  # If set to text, all characters will be accepted
num_box = Text.create_text_input(300, 250, font, mode="number")  # If set to number, only numbers will be accepted
prompt_return = Text.create_text_input(300, 150, font)  # Text input for displaying prompts

# -------------------------
# State to Color Mapping
# -------------------------
state_colors = {
    "start": (30, 30, 30),      # Dark gray background for start screen
    "red": (200, 50, 50),       # Red background when red state is active
    "orange": (255, 140, 0),    # Orange background when orange state is active
    "blue": (50, 100, 255),     # Blue background when blue state is active
}

# -------------------------
# Main Loop
# -------------------------
running = True
while running:
    screen.fill(state_colors.get(states.current, (30, 30, 30)))

    # ---- Event Handling ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        text_box.handle_event(event)  # Pass keyboard events to text input
        num_box.handle_event(event)   # Pass keyboard events to number input

        # If not on start screen and Enter is pressed, return to start
        if states.current != "start" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            states.set_state("start")

    # ---- Render Based on State ----
    if states.current == "start":
        # Draw buttons and check if they were clicked
        if red_btn.draw(screen):
            states.set_state("red")
        if orange_btn.draw(screen):
            states.set_state("orange")
        if blue_btn.draw(screen):
            states.set_state("blue")

        # Draw prompts
        Text.create_text_input(300, 100, font).drawPrompt(screen, "Enter your name:")
        Text.create_text_input(300, 200, font).drawPrompt(screen, "Enter your age:")
        Text.create_text_input(250, 300, font).drawPrompt(screen, "Select your favorite color:")

        # Draw input boxes
        text_box.draw(screen)
        num_box.draw(screen)
    else:
        # If in a color state, show return prompt
        prompt_return.drawPrompt(screen, "Press enter")

    # ---- Update Display ----
    pygame.display.update()
    clock.tick(60)  # Cap framerate at 60 FPS

pygame.quit()