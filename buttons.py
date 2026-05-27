
import pygame
class Button:
    
    def __init__(self, x, y, image, scale=1.0):
        width = int(image.get_width() * scale)
        height = int(image.get_height() * scale)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.font = pygame.font.SysFont(None, 32)
        self.text = ""
        self.text_color = (255, 255, 255)


        # Hover effect
        self.hover_image = self.image.copy()
        light = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        light.fill((60, 60, 60, 80))
        self.hover_image.blit(light, (0, 0))

    
    def set_text(self, text):
        self.text = text


    def draw(self, window):
        action = False
        mousePos = pygame.mouse.get_pos()

        # Define default image each loop
        current_image = self.image

        if self.rect.collidepoint(mousePos):
            current_image = self.hover_image

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        # Reset click when mouse released (outside or inside)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        window.blit(current_image, self.rect)

        # Display text after drawing the button
        if self.text != "":
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            window.blit(text_surface, text_rect)


        return action