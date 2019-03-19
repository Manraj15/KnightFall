from GUI import *

class TutorialMenu(GUI):
    '''
    The tutorial menu contains a brief description
    of how to play the KnightFall game.
    '''

    def __init__(self, bkg_img, view, btn_dict):
        '''
        Create the Tutorial menu for KnightFall.
        '''
        GUI.__init__(self, bkg_img, view, btn_dict)

    def _display_elements(self):

        self.btn_dict.get("title").display_button()
        self.btn_dict.get("logo").display_button()
        self.btn_dict.get("back").display_button()
        self.btn_dict.get("info").display_button()

    def _handle_btn_events(self, cursor, event):

        if self.btn_dict.get("back").is_clicked(cursor, event):
            return 0

 
