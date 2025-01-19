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
enter = 0
names = []
gameVars = {"camY":camY, "names":names, "enter":enter}
score = 0
difficulty = 0
repeat = 0
highscores = []
place = 1
#508x288
sprite_sheet = SpriteLoader("grass block.png")
grass = sprite_sheet.get_image(0, 0, 70, 35)

def get_images():
  global playerimg, play, grass
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
  first = tile((play.rect.x + 35, play.rect.bottom + 30), grass, tiles, True)
  tiles.add(first)
  #something like render distance (1 screen worth)
def spawntiles(bottomY, topY):
  global difficulty
  for i in range(25 - difficulty):
    til = tile((random.randint(0, width), random.randint(topY, bottomY)), grass, tiles, False)
    tiles.add(til)
  if difficulty < 15:
    difficulty += 1

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
def highscore(score, name):
  highscores = open("score.txt", "a")
  highscores.write(f"{score}" + " " + f"{name}")
  highscores.write("\n")
  highscores.close()

def scoring():
  score = int(gameVars["camY"])
  pygame.font.init()
  text = pygame.font.Font('font.ttf', 30)
  text_surface = text.render(f"{score}", False, (0, 0, 0))
  screen.blit(text_surface, (100,100))

def die():
  pygame.font.init()
  text = pygame.font.Font('font.ttf', 100)
  text_surface = text.render("gameover", False, (255, 0, 0))
  screen.blit(text_surface, (pygame.display.Info().current_w / 2.7,pygame.display.Info().current_h / 4))
def getscorename():
  scores = open("score.txt", "r")
  leaderboard = []
  for line in scores:
    leaderboard.append([int(line.split(" ")[0]), line.split(" ")[1][:-1]])
  scores.close()
  leaderboard = sorted(leaderboard, key = lambda x: x[0])
  return leaderboard

def displayscores():
  highscores = getscorename()
  highscores.reverse()
  for i in range(0, min(len(highscores), 9)):
    pygame.font.init()
    text = pygame.font.Font('font.ttf', 30)
    text_surface = text.render(f"{i + 1}. {highscores[i][0]} {highscores[i][1]}", False, (0, 0, 0)) 
    screen.blit(text_surface, (pygame.display.Info().current_w / 2.2, pygame.display.Info().current_h / 3 + i*40))

def username():
  s = ''.join(names)
  pygame.font.init()
  text = pygame.font.Font('font.ttf', 30)
  text_surface = text.render(s, False, (0, 0, 0)) 
  screen.blit(text_surface, (pygame.display.Info().current_w / 1.5, pygame.display.Info().current_h / 2))

def addscores():
  global repeat
  scores = open("score.txt", "r")
  for line in scores:
    highscores.append(int(line.split(" ")[0]))
  scores.close()
  highscores.sort(reverse=True)
  repeat += 1

def main():
  global play, gameVars, spawn, repeat, enter
  get_images()
  while True:  
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == KEYDOWN and play.gameovers == True and enter == 0:
        #s = ''.join(gameVars["names"])
        if event.key == K_RETURN:
          highscore(round(gameVars["camY"]), str("".join(gameVars["names"])))
          enter = 1
        names.append(event.unicode)
      if event.type == QUIT:
        sys.exit()

    keys = pygame.key.get_pressed()
    screen.fill(color)
    tiles.draw(screen)
    for tile in tiles:
      tile.update()
    play.draw(screen)
    play.update()
    scoring()
    if play.gameovers == True:
      die()
      username()
      displayscores()
    if repeat == 0 and play.gameovers == True:
      addscores()
    pygame.display.flip()
    if (gameVars["camY"] % 500 <= 20 and spawn == True):
      spawntiles(pygame.display.Info().current_h * -1, pygame.display.Info().current_h * -2)
      spawn = False
    else:
      if gameVars["camY"] % 500 > 20:
        spawn = True
spawntiles(pygame.display.Info().current_h, 0)
spawntiles(0, pygame.display.Info().current_h * -1)
spawntiles(pygame.display.Info().current_h * -1, pygame.display.Info().current_h * -2)
if __name__ == "__main__":
  main()