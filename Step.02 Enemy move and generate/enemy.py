import pygame
import math
import os
from settings import *

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))

class Enemy:
    def __init__(self, PATH = PATH_One):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        self.path = PATH
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        self.hit_box = (self.x - self.width // 2, self.y - self.height // 2)
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        Draw health bar on an enemy
        :param win: window
        :return: None
        """
        # ...(to be done)
        pygame.draw.rect(win, GREEN, (self.hit_box[0], self.hit_box[1] - 12, 40, 8))
        pygame.draw.rect(win, RED, (self.hit_box[0] + self.max_health* 4, self.hit_box[1] - 12, 50, 8))

        pass

    def move(self):
        """
        Enemy move toward path points every frame
        :return: None
        """
        # ...(to be done)
        x1, y1 = self.path[self.path_pos]
        x2, y2 = self.path[self.path_pos+1]
        
        distance_A_B = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        max_count = int(distance_A_B / self.stride)  # total footsteps that needed from A to B

        if self.move_count < max_count:
            unit_vector_x = (x2 - x1) / distance_A_B
            unit_vector_y = (y2 - y1) / distance_A_B
            delta_x = unit_vector_x * self.stride
            delta_y = unit_vector_y * self.stride

            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count+=1
            pass
        else:
            self.path_pos += 1
            self.move_count = 0


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        self.reserved_members = []
        self.expedition = [Enemy()]  # don't change this line until you do the EX.3 
        self.path_change = False  #False -> PATH_One, True -> PATH_Two

    def campaign(self):
        """
        Send an enemy to go on an expedition once 120 frame
        :return: None
        """

        # Hint: self.expedition.append(self.reserved_members.pop())
        # ...(to be done)
        
        if self.gen_count >= self.gen_period and not self.is_empty():  #determined whether the enemy is empty
            self.expedition.append(self.reserved_members.pop())     #create new enemies
            self.gen_count = 0
        else:
            self.gen_count+=1
        pass

    def generate(self, num):
        """
        Generate the enemies in this wave
        :param num: enemy number
        :return: None
        """
        # ...(to be done)
        
        if self.path_change:  # path changed
            PATH = PATH_One   #option one
            self.path_change=False
        else:
            PATH = PATH_Two   #option two
            self.path_change=True

        for i in range(0,num):  #append enemies
            self.reserved_members.append(Enemy(PATH)) #append to current path
        
        pass

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)





