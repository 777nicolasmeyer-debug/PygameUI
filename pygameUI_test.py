import pygame
from buttons import Button
from text_input import Text

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UI Test")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

def make_surface(color):
    surf = pygame.Surface((150, 80))
    surf.fill(color)
    return surf
# Create images
red_img = make_surface((200, 50, 50))
orange_img = make_surface((255, 140, 0))
blue_img = make_surface((50, 100, 255))

# Create buttons
red_button = Button(100, 200, red_img)
orange_button = Button(325, 200, orange_img)
blue_button = Button(550, 200, blue_img)

text_box = Text(300, 100, font, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        text_box.handle_event(event)

    # draw
    screen.fill((30, 30, 30))

    # buttons
    if red_button.draw(screen):
        print("Red clicked")

    if orange_button.draw(screen):
        print("Orange clicked")

    if blue_button.draw(screen):
        print("Blue clicked")

    # text
    if hasattr(text_box, "draw"):
        text_box.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()




