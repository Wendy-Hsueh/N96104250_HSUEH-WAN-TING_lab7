from enemy import EnemyGroup
import pygame
import os
import math
import settings
TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide(self, enemy):
        """
        Q2.2)check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool
        """

        """
        Hint:
        x1, y1 = enemy.get_pos()
        ...
        """
        enemyX, enemyY = enemy.get_pos()
        towerX, towerY = self.center
        self.distance_x = enemyX - towerX
        self.distance_y = enemyY - towerY
        # Use math.sqrt() to find the square root
        self.len= math.sqrt((self.distance_x**2)+(self.distance_y**2))

        if self.len <= self.radius:
            return(True)
        else:
            return(False)
        pass

    def draw_transparent(self, win):
        """
        Q1) draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """
        # Create a canvas with twice the radius
        transparent_surface = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        # define transparency: 0~255, 0 is fully transparent
        transparency = 50  
        # draw the circle on the transparent surface/pygame.draw.circle(Surface, color, pos , raduis, width)
        pygame.draw.circle(transparent_surface, (255, 255, 255, transparency), (self.radius,self.radius) , self.radius, 200)
        # Calculate the starting point of the picture
        tower_centerX, tower_centerY = self.center
        win.blit(transparent_surface, (tower_centerX-self.radius, tower_centerY-self.radius))
        pass


class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = True  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):
        """
        Q2.1) Return whether the tower is cooling down
        (1) Use a counter to computer whether the tower is cooling down (( self.cd_count
        :return: Bool
        """

        """
        Hint:
        let counter be 0
        if the counter < max counter then
            set counter to counter + 1
        else 
            counter return to zero
        end if
        """
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return(True)
        else:
            self.cd_count = 0
            return(False)
        pass

    def attack(self, enemy_group):
        """
        Q2.3) Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: None
        """
        if self.is_cool_down(): 
            return
        else :
            for enemies in enemy_group.get():            # Determine if enemy is in the enemy_group
                if self.range_circle.collide(enemies):   # Determine if the enemies is within range
                    enemies.get_hurt(self.damage)        # Blood loss
                    return
                else:
                    continue
            
        pass

    def is_clicked(self, x, y):
        """
        Bonus) Return whether the tower is clicked
        (1) If the mouse position is on the tower image, return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """
        towerX, towerY = self.rect.center    # tower center position X and Y
        # The picture is 70x70, so click on the x and y range to be 35 from the center point
        if towerX -35 < x < towerX + 35 and towerY -35 < y < towerY + 35:    # define clicked range
            return(True) 
        else:
            return(False)
        pass

    def get_selected(self, is_selected):
        """
        Bonus) Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None
        """
        self.is_selected = is_selected  # Select or not

    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower

