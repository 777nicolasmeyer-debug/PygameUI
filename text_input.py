import pygame
from pygame import surface


class Text:
    def __init__(self, x, y, font, color, mode="text", width=200, height=40):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.text = ""
        self.mode = mode  # "text" or "number"
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        # check if mouse clicked inside textbox
            mouse_pos = event.pos

        # simple textbox area 
            box_rect = pygame.Rect(self.x, self.y, 200, 40)

            if box_rect.collidepoint(mouse_pos):
                self.active = True
            else:
                self.active = False

    # ONLY type if active (textbox clicked)
        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                char = event.unicode

                if self.mode == "text":
                    if char.isalnum() or char == " ":
                        self.text += char

                elif self.mode == "number":
                    if char.isdigit() or char == ".":
                        self.text += char


    def draw(self, surface):
        # active color
        if self.active:
            box_color = (200, 200, 200)
        else:
         box_color = (100, 100, 100)

        pygame.draw.rect(surface, box_color, self.rect, 2)

        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


    def drawPrompt(self, surface, prompt_text):
        prompt_surface = self.font.render(prompt_text, True, (255, 255, 255))
        surface.blit(prompt_surface, (self.x, self.y))


    def create_text_input(x, y, font, color=(255, 255, 255), mode="text", width=200, height=40):
        # Helper Functions make everythign look nicer so im just gonna roll with it
        return Text(x, y, font, color, mode, width, height)
