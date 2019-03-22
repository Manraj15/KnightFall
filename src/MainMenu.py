from ViewController import *

from ModeMenu import *
from LBMenu import *
from TutorialMenu import *
from CreditsMenu import *
from PauseMenu import *

import time

class MainMenu(ViewController):
    '''
    The MainMenu for the game KnightFall.
    '''
    
    def __init__(self, bkg_img, view, btn_dict, lb, tut, creds, mode):
        '''
        Create the KnightFall's MainMenu to display in view.
        '''
        ViewController.__init__(self, bkg_img, view, btn_dict)

        self.mode_menu = mode
        self.lb = lb
        self.tut = tut
        self.credits = creds

    def _display_elements(self):
        
        self.btn_dict.get("title-main").display_button()
        self.btn_dict.get("start").display_button()
        self.btn_dict.get("tutorial").display_button()
        self.btn_dict.get("leaderboards").display_button()
        self.btn_dict.get("credits").display_button()
        self.btn_dict.get("quit").display_button()

    def _handle_btn_events(self, cursor, event):
        
        if self.btn_dict.get("start").is_clicked(cursor, event):
            self.mode_menu.display_GUI()
                
        elif self.btn_dict.get("tutorial").is_clicked(cursor, event):
            self.tut.display_GUI()
                
        elif self.btn_dict.get("leaderboards").is_clicked(cursor, event):
            self.lb.display_GUI()

        elif self.btn_dict.get("credits").is_clicked(cursor, event):
            self.credits.display_GUI()
                
        elif self.btn_dict.get("quit").is_clicked(cursor, event):
            return 1
