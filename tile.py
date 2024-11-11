import pygame

class tile(pygame.sprite.Sprite):
  def __init__(self, pos, image):
    super().__init__()
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.screen_info = pygame.display.Info()

  def update(self):
    pass
    '''
    if(self.rect.left > self.screen_info.current_w):
      self.rect.right = 0
    frame = pygame.time.get_ticks() // 60 % 8
    self.image = self.images[frame]
    '''