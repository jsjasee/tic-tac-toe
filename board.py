class Board:
    def __init__(self):
        self.spaces = {
            "a1" : " ",
            "a2" : " ",
            "a3" : " ",
            "b1" : " ",
            "b2" : " ",
            "b3" : " ",
            "c1" : " ",
            "c2" : " ",
            "c3" : " ",
        }

    def update_board(self):
        play_area = f"""
           1   2   3
        A  {self.spaces["a1"]} | {self.spaces["a2"]} | {self.spaces["a3"]}  
          ------------
        B  {self.spaces["b1"]} | {self.spaces["b2"]} | {self.spaces["b3"]}  
          ------------
        C  {self.spaces["c1"]} | {self.spaces["c2"]} | {self.spaces["c3"]} 
        """
        return play_area

    def win_lose(self):

        # instead of manually checking winning conditions one by one, define the winning conditions first and then loop through them!
        # refine version

        winning_combinations = [
            ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"], # for rows
            ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"], # for columns
            ["a1", "b2", "c3"], ["a3", "b2", "c1"] # for diagonals
        ]

        for combo in winning_combinations:
            # note combo[0] gives a space like a1 for example
            if self.spaces[combo[0]] == self.spaces[combo[1]] == self.spaces[combo[2]] != " ":
                return True

        return False

        # if (((self.spaces["a1"] == self.spaces["a2"] == self.spaces["a3"] != " ") or
        #     (self.spaces["b1"] == self.spaces["b2"] == self.spaces["b3"] != " ") or
        #     (self.spaces["c1"] == self.spaces["c2"] == self.spaces["c3"] != " ") or
        #     (self.spaces["a1"] == self.spaces["b1"] == self.spaces["c1"] != " ") or
        #     (self.spaces["a2"] == self.spaces["b2"] == self.spaces["c2"] != " ") or
        #     (self.spaces["a3"] == self.spaces["b3"] == self.spaces["c3"] != " ") or
        #     (self.spaces["a1"] == self.spaces["b2"] == self.spaces["c3"] != " ")) or
        #         (self.spaces["a3"] == self.spaces["b2"] == self.spaces["c1"] != " ")):
        #     return True
        # else:
        #     return False
