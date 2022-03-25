import pygame
import os

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))  # load image of menu 
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))    # load image of upgrade 
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))          # load image of sell 
class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_width, self.menu_height = 200, 200    # set width and height of menu
        self.MENU_IMAGE = pygame.transform.scale(MENU_IMAGE, (self.menu_width, self.menu_height))   # draw menu
        # set location of button
        self.__buttons = [Button(UPGRADE_IMAGE, "upgrade", x, y - 70),
                          Button(SELL_IMAGE, "sell", x, y + 75)]  # (Q2) Add buttons here
        # get center of menu
        self.rect = self.MENU_IMAGE.get_rect()
        self.rect.center = (x, y)
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.MENU_IMAGE, self.rect)
        # draw button
        # (Q2) Draw buttons here
        for button in self.__buttons:
            win.blit(button.image, button.rect)
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons   # return the button list
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        if self.name == 'upgrade':
            self.image = pygame.transform.scale(image, (60, 40))    # set buiion size (upgrade)
        if self.name == 'sell':
            self.image = pygame.transform.scale(image, (40, 40))    # set buiion size (sell)
        # get center of menu
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x, y) :   # check wheather the button is clicked
            return True
        else :
            return False
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name    # return the button name
        pass






