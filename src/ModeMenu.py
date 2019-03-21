from ViewController import *

class ModeMenu(ViewController):
    '''
    The mode selection menu for the KnightFall game
    includes the classic and survival mode.
    '''

    def __init__(self, bkg_img, view, btn_dict):
        '''
        Create a new ModeMenu.
        '''
        ViewController.__init__(self, bkg_img, view, btn_dict)

    def _display_elements(self):

        self.btn_dict.get("title").display_button()
        self.btn_dict.get("logo").display_button()
        self.btn_dict.get("classic").display_button()
        self.btn_dict.get("survival").display_button()
        self.btn_dict.get("back").display_button()

    def _handle_btn_events(self, cursor, event):
        
        if self.btn_dict.get("classic").is_clicked(cursor, event):
            pass
        elif self.btn_dict.get("survival").is_clicked(cursor, event):
            pass
        elif self.btn_dict.get("back").is_clicked(cursor, event):
            return 0

 

