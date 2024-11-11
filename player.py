import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, pos, images, tiles, gamevar):
        super().__init__()
        self.variables = gamevar
        self.tiles = tiles
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.screen_info = pygame.display.Info()
        self.velocity = 1
        self.ground = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        #self.rect.move_ip(self.speed)
        frame = pygame.time.get_ticks() // 60 % 3
        self.image = self.images[frame]
        if (self.rect.top <= pygame.display.Info().current_h / 4 and self.velocity > 0):
            for tile in self.tiles:
                tile.rect.y += self.velocity
            self.variables["camY"] += self.velocity
            print(self.variables["camY"])
        else:
            self.rect.y -= self.velocity
        self.velocity -= 0.5
        if (self.rect.bottom >= pygame.display.Info().current_h):
            self.velocity = 0
        hit = pygame.sprite.spritecollide(self, self.tiles, False) 
        for tile in hit:
            if self.velocity < 0:
                if (self.rect.bottom <= tile.rect.bottom):
                    self.velocity = 0
                    self.ground = True

        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if (self.rect.bottom >= pygame.display.Info().current_h or self.ground):
                if (self.velocity == 0):
                    self.velocity += 20
                    self.ground = False
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        
            
    #camera boundry thing idea: pygame.display.Info().current_h - pygame.display.Info().current_h / 4
    '''
    if(self.rect.left > self.screen_info.current_w):
      self.rect.right = 0
    frame = pygame.time.get_ticks() // 60 % 8
    self.image = self.images[frame]
    '''