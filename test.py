
import pygame
from buttons import Button
from text_input import Text

pygame.init()
# -------------------------
# Setup
# -------------------------
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UI Tutorial Test")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

# -------------------------
# Create simple colored surfaces (buttons need images)
# -------------------------
red_surface = pygame.Surface((150, 80))
red_surface.fill((200, 50, 50))

orange_surface = pygame.Surface((150, 80))
orange_surface.fill((255, 140, 0))

blue_surface = pygame.Surface((150, 80))
blue_surface.fill((50, 100, 255))

# -------------------------
# Create Buttons
# -------------------------
red_button = Button(100, 300, red_surface)
red_button.set_text("Red")

orange_button = Button(325, 300, orange_surface)
orange_button.set_text("Orange")

blue_button = Button(550, 300, blue_surface)
blue_button.set_text("Blue")

# -------------------------
# Create Text Input
# -------------------------
text_box1 = Text(300, 150, font, (255, 255, 255), "text")
prompt_box1 = Text(300, 100, font, (255, 255, 255), "text")
number_box1 = Text(300, 250, font, (255, 255, 255), "number")
prompt_box2 = Text(300, 200, font, (255, 255, 255), "text")


# -------------------------
# Main Loop
# -------------------------
running = True
while running:
    screen.fill((30, 30, 30))

    # ---- EVENT HANDLING ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # pass typing events to text box
        text_box1.handle_event(event)
        number_box1.handle_event(event)

    # ---- BUTTONS ----
    if red_button.draw(screen):
        print("Red button clicked")

    if orange_button.draw(screen):
        print("Orange button clicked")

    if blue_button.draw(screen):
        print("Blue button clicked")

    # ---- DRAW TEXT ----
    prompt_box1.drawPrompt(screen, "Type something:")
    prompt_box2.drawPrompt(screen, "Type a number:")
    text_box1.draw(screen)
    number_box1.draw(screen)

    # ---- UPDATE ----
    pygame.display.update()
    clock.tick(60)

pygame.quit()
# -------------------------
# The lines look nice, but idk if im ever gonna use it again