from typing import Text
import pygame

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_WIDTH = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()
# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
role_img = pygame.transform.scale(pygame.image.load("images/enemy.png"), (70, 70))
pause_img = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_WIDTH))
continue_img = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_WIDTH))
muse_img = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_WIDTH))
sound_img = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_WIDTH))
hp_gray_img = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
hp_img = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))

# set the title
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        # window
        self.shape = (WIN_WIDTH,WIN_HEIGHT) #width, height
        self.window = pygame.display.set_mode(self.shape) ## CREATE WINDOW GAME
		
        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            clock.tick(FPS)
            # event loop (user action)
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    run = False
            # draw background
            self.window.blit(background_image, (0,0))
            # draw enemy and health bar
            self.window.blit(role_img,(10,200))
            pygame.draw.rect(self.window, RED, [8, 180, 100, 15])
            # draw menu (and buttons)
            pygame.draw.rect(self.window, BLACK, [0, 0, WIN_WIDTH, 100])
            self.window.blit(pause_img,(920,0))
            self.window.blit(continue_img,(840,0))
            self.window.blit(sound_img,(760,0))
            self.window.blit(muse_img,(670,0))

            blank = 300
            blank_high = 40
            for i in range(5):
                self.window.blit(hp_gray_img,(blank,0))
                self.window.blit(hp_img,(blank,0))
                blank = blank+60

            blank = 300
            for i in range(5):
                self.window.blit(hp_gray_img,(blank,blank_high))
                if (i==0 or i==1):
                    self.window.blit(hp_img,(blank,blank_high))
                blank = blank+60

            pygame.display.update()
            # draw time
            pygame.draw.rect(self.window, BLACK, [8, 545, 110, 50])
            ticks=pygame.time.get_ticks()
            millis=ticks%1000
            seconds=int(ticks/1000 % 60)
            minutes=int(ticks/60000 % 24)
            out='{minutes:02d}:{seconds:02d}'.format(minutes=minutes, millis=millis, seconds=seconds)
            font = pygame.font.SysFont(None,50)
            text = font.render(out,True,WHITE)	
            self.window.blit(text, (20,555))
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()
