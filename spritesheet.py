import pygame
class SpriteLoader:
  def __init__(self, img_path):
    self.sprite_sheet = pygame.image.load(img_path)

  def get_image(self, x, y, width, height):
    image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
    return image