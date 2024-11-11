import pygame, sys, random
from pygame.locals import *
from spritesheet import SpriteLoader
from tile import tile
from player import player


pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (100,100,200)
tiles = pygame.sprite.Group()
#508x288
def get_images():
  global playerimg, play
  sprite_sheet = SpriteLoader("grass block.png")
  grass = sprite_sheet.get_image(0, 0, 70, 35)
  playerspritesheet = SpriteLoader("player.png")
  playerimg= playerspritesheet.get_image(0, 0, 70, 97)
  playerimg2= playerspritesheet.get_image(75, 0, 70, 97)
  playerimg3= playerspritesheet.get_image(0, 100, 70, 97)
  images = []
  images.append(playerimg)
  images.append(playerimg2)
  images.append(playerimg3)
  for i in range(20):
    til = tile((random.randint(0, width), random.randint(0, height)), grass)
    tiles.add(til)
  play = player((random.randint(0, width), random.randint(0, height)), images, tiles)
  '''
  for i in range(4):
    for j in range(2):
      cat_image = sprite_sheet.get_image(j * 512, i * 256, 512, 256)
      cat_image = pygame.transform.smoothscale(cat_image, (180, 90))
      cat_images.append(cat_image)

  for direction in directions:
    for i in range(9):
      guy_image = guy_sheet.get_image(i * 64, directions.index(direction) * 64, 64, 64)
      guy_images[direction + str(i)] = guy_image
'''
play = None

def main():
  global play
  get_images()
  while True:  
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()

    keys = pygame.key.get_pressed()
    screen.fill(color)
    tiles.draw(screen)
    play.draw(screen)
    play.update()
    pygame.display.flip()
if __name__ == "__main__":
  main()