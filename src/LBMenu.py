from GUI import *

pygame.init()

class LBMenu(GUI):
    '''
    The Leaderboards menu for the KnightFall game displays
    the leaderboard for the classic and survival mode.
    '''
    def __init__(self, bkg_img, view, btn_dict, lb_modes = []):
        '''
        (LBMenu, str, str, PyGameDisplay, Dict{Button}, List[Leaderboard]) -> None
        '''
        GUI.__init__(self, bkg_img, view, btn_dict)
        
        self.lb_modes = lb_modes
        self.selected_mode = self.btn_dict.get("classic")

    def _display_elements(self):

        self.btn_dict.get("title").display_button()
        self.btn_dict.get("logo").display_button()
        
        self.selected_mode.display_button()
        
        self.btn_dict.get("back").display_button()
        
        self.btn_dict.get("rank1").display_button()
        self.btn_dict.get("rank2").display_button()
        self.btn_dict.get("rank3").display_button()
        self.btn_dict.get("rank4").display_button()
        self.btn_dict.get("rank5").display_button()

    def _handle_btn_events(self, cursor, event):

        if self.btn_dict.get("classic").is_clicked(cursor, event):
            pass
        elif self.btn_dict.get("survival").is_clicked(cursor, event):
            pass
        if self.btn_dict.get("back").is_clicked(cursor, event):
            return 0
                
