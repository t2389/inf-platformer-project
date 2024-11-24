import pygame

class tile(pygame.sprite.Sprite):
  def __init__(self, pos, image, tiles, first):
    super().__init__()
    self.first = first
    self.image = image
    self.tiles = tiles
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.screen_info = pygame.display.Info()

  def update(self):
    hit = pygame.sprite.spritecollide(self, self.tiles, False) 
    for tile in hit:
      if tile != self and self.first == False:
        self.kill()
    if self.rect.top >= pygame.display.Info().current_h and self.first == False:
      self.kill()
    '''
    if(self.rect.left > self.screen_info.current_w):
      self.rect.right = 0
    frame = pygame.time.get_ticks() // 60 % 8
    self.image = self.images[frame]
    '''