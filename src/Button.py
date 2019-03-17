import pygame
from pygame import *
pygame.init()

class Button(pygame.sprite.Sprite):
    '''
    Create a button from an image to display on the screen.
    '''

    def __init__(self, name, image_file, view, position = [0,0]):
        '''
        (Button, str, str, pygame.display, List[int, int]) -> None
        Create a Button from an image_file. Set the Button's name
        and the view to display in.
        Position is the top left coords of Button.
        '''
        
        self.name = name
        self.image = pygame.image.load(image_file)
        
        # screen position of pygame image and image's rect
        self.rect = self.image.get_rect(topleft=position)
        self.view = view

    def set_name(self, name):
        '''
        (Button, str) -> None
        Set the name of Button.
        '''
        self.name = name
        
    def get_name(self):
        '''
        (Button) -> None
        Return name of Button.
        '''
        return self.name

    def set_pos(self, position):
        '''
        (Button) -> None
        Update the position of Button in the window.
        '''
        self.rect = self.image.get_rect(topleft=position)
        
    def get_btnrect(self):
        '''
        (Button) -> None
        Return Button rect.
        '''
        return self.rect

    def display_button(self):
        '''
        (Button) -> None
        Display Button in view.
        '''
        self.view.blit(self.image, self.rect)
        
