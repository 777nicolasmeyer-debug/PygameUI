import pygame

class Text:
    def __init__(self, x, y, font, color, mode="text"):
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.text = ""
        self.mode = mode  # "text" or "number"

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]

            else:
                char = event.unicode
                # All characters
                if self.mode == "text":
                    if char.isalnum() or char == " ":
                        self.text += char
                # Only numbers
                elif self.mode == "number":
                    if char.isdigit() or char == ".":
                        self.text += char

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.x, self.y))
