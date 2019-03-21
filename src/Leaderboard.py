class Leaderboard:
    '''
    A Leaderboard displays the all-time top 5 high scores
    earned in the game KnightFall. 
    '''
    
    MAX_LEN = 5
    
    def __init__(self):
        '''
        (Leaderboard) -> None
        Create a new Leaderboard for the KnightFall game
        with an empty list of high_scores.
        '''
        # List(Tuple(int, str))
        self._high_scores = []

    def add_score(self, new_score):
        '''
        (Leaderboard, List(Tuple(int, str))) -> None
        Add a new_score to the Leaderboard in the correct place
        if new_score makes the top 5. If there are already 5 high scores
        on the Leaderboard, add new_score iff it is strictly greater
        than the lowest score.
        '''
        
        # _high_scores is in non-ascending order
        
        if self._high_scores == []:
            self._high_scores.append(new_score)
            
        else:

            if len(self._high_scores) == self.MAX_LEN:
                if new_score[0] > self._high_scores[self.MAX_LEN - 1][0]:
                    self._add_score_helper(new_score)
                    
                    # If new_score was added, check if length
                    # of high scores exceeds MAX_LEN
                    if len(self._high_scores) > self.MAX_LEN:
                        self.pop_lowest_score()
            else:
                if new_score[0] <= self._high_scores[len(self._high_scores) - 1][0]:
                    self._high_scores.append(new_score)
                else:
                    self._add_score_helper(new_score)

    def _add_score_helper(self, new_score):
        '''
        (Leaderboard, List(Tuple(int, str))) -> None
        Add new_score in its correct place on the Leaderboard.
        '''
        index = len(self._high_scores) - 1
        
        while(index >= 0):
            if new_score[0] <= self._high_scores[index][0]:
                self._high_scores.insert((index + 1), new_score)
                break
            elif index == 0:
                self._high_scores.insert(0, new_score)
            index -= 1

    def pop_lowest_score(self):
        '''
        (Leaderboard) -> None
        Pop the lowest score on the Leaderboard iff
        high_scores is not empty.
        '''
        if self._high_scores != []:
            self._high_scores.pop()
        
    def print_high_scores(self):
        '''
        (Leaderboard) -> None
        Print an ordered list of the Leaderboard scores
        and the names of the players who set them.
        '''
        place = 1
        for i in range(0, len(self._high_scores)):
            print("{}. {} | {}".format(place, self._high_scores[i][1], self._high_scores[i][0]))
            place += 1

    def get_high_scores(self):
        '''
        (Leaderboard) -> None
        Return the Leaderboard's high_scores list.
        '''
        return self._high_scores
    def save_leader_rank_in_txt(self):
        '''
        (Leaderboard) -> stdout
        Write the Leaderboard's list into txt file
        '''
        rank = open("rank.txt","wb")
        for i in range (0, len(self._high_scores)-1):
            a=self._high_scores[i]
            rank.write(i + ". " + a)
        rank.close()
         
            
