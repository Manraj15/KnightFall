import pygame
import time

pygame.init()

class Button(pygame.sprite.Sprite):
    '''
    Create a button from an image to display on the screen.
    '''
    # Button actions are handled in files that use and call Button

    def __init__(self, name, image_file, view, position = [0,0], btn_action = None):
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
        self.action = btn_action

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

    def _set_view(self, view):
        '''
        (Button, pygame.display) -> None
        Update the view Button will display on.
        '''
        self.view = view

    def set_pos(self, position):
        '''
        (Button) -> None
        Update the position of Button in the window
        given the top left coordinate.
        '''
        self.rect = self.image.get_rect(topleft=position)
        
    def get_btnrect(self):
        '''
        (Button) -> None
        Return Button rect.
        '''
        return self.rect

    def is_hover(self, cursor):
        '''
        (Button, cursor) -> bool
        Return True iff cursor hovers over Button.
        '''
        if self.get_btnrect().collidepoint(cursor):
            return True
        return False

    def is_clicked(self, cursor, event):
        if self.is_hover(cursor) and event == pygame.MOUSEBUTTONDOWN:
            return True
        return False
        
    def set_action(self, action):
        '''
        Set the action that Button invokes.
        The action parameter takes a tuple of two elements.
        The first element is an int 0 or 1. If the second element is
        an object, use 0. If the second element is a function, use 1.
        '''
        self.action = action

    def call_action(self):
        '''
        Execute the button's action if an action is defined.
        '''
        if self.action != None:
            
            # return a value
            if self.action[0] == 0:
                return self.action[1]

            # call a function
            elif self.action[0] == 1:
                return self.action[1]()

    def display_button(self):
        '''
        (Button) -> None
        Display Button in view.
        '''
        self.view.blit(self.image, self.rect)

def create_btn_dict(btn_list):
    '''
    Return a new dictionary of buttons given a btn_lst.
    The key is the Button name and the value is the Button instance.
    '''
    btn_dict = dict()
    for i in range(len(btn_list)):
        btn_dict[btn_list[i].get_name()] = btn_list[i]

    return btn_dict
