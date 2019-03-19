import pygame
from pygame import *
import time
from Button import *
from Leaderboard import Leaderboard

pygame.init()

class GUI():
    '''
    A visual interface for the KnightFall menu displays.
    '''
    def __init__(self, bkg_img, view, btn_dict = dict()):
        '''
        (GUI, str, str, pygame.display, dict) -> None
        Create a UI named name with a dict of visual elements
        and a backgound image to display on a view screen.
        '''
        self._view = view
        self.btn_dict = btn_dict
    
        self._set_bkg(bkg_img)

    def _set_bkg(self, image_file):
        '''
        (GUI, str) -> None
        Load and prepare a KnightFall menu background.
        '''
        # Note: expected background size is 1280px by 720px
        self.bkg = pygame.image.load(image_file)
        # scale bkg image to window size
        width, height = pygame.display.get_surface().get_size()
        self.bkg = pygame.transform.scale(self.bkg, (width, height))
        
        self.rect = self.bkg.get_rect()
        self.rect.left, self.rect.top = [0,0]        

    def _display_elements(self):
        '''
        Blit the elements defined by an instance of GUI to the view.
        '''
        pass
    
    def _handle_btn_events(self, cursor, event):
        '''
        Handle the actions for a Button blit on the view.
        '''
        pass

    def display_GUI(self, clock = None):
        '''
        (GUI, pygame.time.Clock) -> None
        '''
        self.clock = pygame.time.Clock() if clock == None else clock

        show_menu = True
        while show_menu:
            
            # Render background
            self._view.fill([255, 255, 255])
            self._view.blit(self.bkg, self.rect)
            
            # Track cursor position and click action
            cursor = pygame.mouse.get_pos()
            click_action = pygame.mouse.get_pressed()

            # Render Buttons
            self._display_elements()

            # Event handling...
            btn_event = None
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thanks for playing!")
                    pygame.quit()
                    quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    btn_event = self._handle_btn_events(cursor, event.type)
            
            if btn_event == 0:
                break
            elif btn_event == 1:
                show_menu = False
                break
            
            pygame.display.flip()
            self.clock.tick(15)
            



