import pygame, sys, random
from pygame.locals import *
from spritesheet import SpriteLoader
from tile import tile
from player import player

pygame.init()
camY = 0
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (100,100,200)
tiles = pygame.sprite.Group()
spawn = True
gameVars = {"camY":camY}
#508x288
def get_images():
  global playerimg, play, grass
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
  score = 0
  play = player((random.randint(0, width), random.randint(0, height)), images, tiles, gameVars)
  #something like render distance (1 screen worth)
def spawntiles(bottomY, topY):
  for i in range(10):
    til = tile((random.randint(0, width), random.randint(topY, bottomY)), grass)
    tiles.add(til)
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
  global play, gameVars, spawn
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
    if (gameVars["camY"] % 500 == 0 and spawn == True):
      spawntiles(pygame.display.Info().current_h * -1, pygame.display.Info().current_h * -2)
      spawn = False
    else:
      spawn = True

if __name__ == "__main__":
  main()