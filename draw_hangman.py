class DrawHangman:
    def __init__(self):
        self.line = '  | \n'
        self.head = '(-_-)\n'
        self.finish_head = '(x_x)\n'
        self.body = ' [ ] \n'
        self.body_with_left_hand = '/[ ] \n'
        self.body_with_hands = '/[ ]' + chr(92) + '\n'
        self.left_leg = ' |'
        self.legs = ' | | '


    def one_error(self):
        return (self.line + self.head).rstrip()
    
    def two_errors(self):
        return (self.line + self.head + self.body).rstrip()
    
    def three_errors(self):
        return (self.line + self.head + self.body_with_left_hand).rstrip()
    
    def four_errors(self):
        return (self.line + self.head + self.body_with_hands).rstrip()
    
    def five_errors(self):
        return (self.line + self.head + self.body_with_hands + self.left_leg).rstrip()
    
    def six_errors(self):
        return (self.line + self.finish_head + self.body_with_hands + self.legs).rstrip()

    def get_hangman_state(self, error_count):
        if error_count == 1:
            return self.one_error()
        elif error_count == 2:
            return self.two_errors()
        elif error_count == 3:
            return self.three_errors()
        elif error_count == 4:
            return self.four_errors()
        elif error_count == 5:
            return self.five_errors()
        elif error_count == 6:
            return self.six_errors()

