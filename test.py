import pygame
from buttons import Button    # In a real project say, from PygameUI import (Button, Text, States ect...)
from text_input import Text
from state_handeling import States
States = States("start")  # Create state manager with default state "start"

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
# Create simple colored surfaces (buttons need images)
# -------------------------                                                                                         
red_surface = pygame.Surface((150, 80)) # Here you can upload a .png file by saying: red_surface = pygame.image.load("Your_file_here.png").convert_alpha() and so on for the other colors
red_surface.fill((200, 50, 50))         # If you use a .png file this line is unnecessary

orange_surface = pygame.Surface((150, 80))
orange_surface.fill((255, 140, 0))

blue_surface = pygame.Surface((150, 80))
blue_surface.fill((50, 100, 255))

# -------------------------
# Create Buttons
# -------------------------
red_button = Button(100, 350, red_surface)
red_button.set_text("Red")               # I recomend setting the text like this so that you can reuse .png files instead of needing one for each button

orange_button = Button(325, 350, orange_surface)
orange_button.set_text("Orange")

blue_button = Button(550, 350, blue_surface)
blue_button.set_text("Blue")

# -------------------------
# Create Text Input
# -------------------------
text_box1 = Text(300, 150, font, (255, 255, 255), "text") # If its set to text, all characters wil be acepted
prompt_box1 = Text(300, 100, font, (255, 255, 255), "text")
number_box1 = Text(300, 250, font, (255, 255, 255), "number") # If its set to number only nubers wil be accepted
prompt_box2 = Text(300, 200, font, (255, 255, 255), "text")
prompt_box3 = Text(250, 300, font, (255, 255, 255), "text")
prompt_box4 = Text(300, 150, font, (255, 255, 255), "text")


# -------------------------
# Main Loop
# -------------------------
BGcolor = (30, 30, 30)

running = True
while running:
    screen.fill((BGcolor))

    # ---- EVENT HANDLING ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # pass typing events to text box
        text_box1.handle_event(event)
        number_box1.handle_event(event)

    # ---- BUTTONS ----
    if States.current == "start":
        if red_button.draw(screen):
            States.set_state("red")

        if orange_button.draw(screen):
            States.set_state("orange")

        if blue_button.draw(screen):
            States.set_state("blue")

    #---- Change background color based on state ----
    if States.current != "start":
        if States.current == "red":
            BGcolor = (200, 50, 50)
        elif States.current == "orange":
            BGcolor = (255, 140, 0)
        elif States.current == "blue":
            BGcolor = (50, 100, 255)

        prompt_box4.drawPrompt(screen, "Press enter")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            States.set_state("start")
            BGcolor = (30, 30, 30)

    # ---- DRAW TEXT ----
    if States.current == "start":
        prompt_box1.drawPrompt(screen, "Enter your name:")
        prompt_box2.drawPrompt(screen, "Enter your age:")
        prompt_box3.drawPrompt(screen, "Select your favorite color:")
        text_box1.draw(screen)
        number_box1.draw(screen)

    # ---- UPDATE ----
    pygame.display.update()
    clock.tick(60)

pygame.quit()
# -------------------------
# The lines look nice, but idk if im ever gonna use it again