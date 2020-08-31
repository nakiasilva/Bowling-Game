from Exceptions import MaxFrameExceededError, checkLastFrameValError

class BowlingGame:

    all_strike_score = 300

    def __init__(self):
        self.score_board = []
        self.first_trial = True
        self.all_strike = True
        self.frame_no = 0
        self.play_strike = False
        self.play_spare = False

    def setScoreFirstTrial(self, pins):
        try:
            self.score_board.append([0] * 2)
            if pins == 10:
                self.first_trial = True
                self.score_board[self.frame_no][0] = pins
                self.frame_no = self.frame_no + 1
            else:
                self.first_trial = False
                self.all_strike = False
                self.score_board[self.frame_no][0] = pins
        except IndexError as e:
            print("Index Error occured in setScoreFirstTrial(): ", str(e))
        except Exception:
            print("Error occured in setScoreFirstTrial(): ",  str(e))

    def setScoreSecondTrial(self, pins):
        try:
            self.first_trial = True
            if self.score_board[self.frame_no][0] + pins == 10:
                self.score_board[self.frame_no][1] = pins
            else:
                self.score_board[self.frame_no][1] = pins
            self.frame_no = self.frame_no + 1
        except IndexError as e:
            print("Index Error occured in setScoreFirstTrial(): ", str(e))
        except Exception:
            print("Error occured in setScoreFirstTrial(): ",  str(e))


    def checkLastFrameVal(self):
        try:
            if self.frame_no == 10:
                if  self.score_board[9][0] == 10:
                    self.play_strike = True
                elif (self.score_board[9][0] + self.score_board[9][1]) == 10:
                    self.play_spare = True

                if not (self.play_spare or self.play_strike):
                    self.score()
                    exit()
                elif self.play_spare:
                    print("Play another bowl")
                elif self.play_strike:
                    print("Play another frame")
        except IndexError as e:
            print("Index Error occured in setScoreFirstTrial(): ", str(e))
        except checkLastFrameValError:
            print("Error occured in checkLastFrameVal(): ", str(e))
            

    def roll(self, pins):
        try:
            if self.frame_no > 10:
                raise MaxFrameExceededError()

            if self.first_trial:
                self.setScoreFirstTrial(pins)
                if self.play_spare:
                    self.play_spare = False
                    return
                if self.play_strike and self.first_trial:
                    return
            else:
                self.setScoreSecondTrial(pins)
                if self.play_strike:
                    self.score()
                    self.play_strike = False
                    return
            self.checkLastFrameVal()
        except MaxFrameExceededError as e:
            print("Maximun number of frames (10) exceeded: ", str(e))


    def score(self):
        try:
            total_score = 0
            board = self.score_board
            bonus1 = 0
            bonus2 = 0
            if self.all_strike:
                total_score = self.all_strike_score
                return
            for i in  range(len(board)):
                if i == len(board) - 1:
                    if not (self.play_strike or self.play_spare):
                        score = board[i][0] + board[i][1]
                    else:
                        score = 0
                elif board[i][0] == 10 and board[i+1][0] == 10:
                    bonus1 = 10
                    score = 10 + bonus1 
                elif board[i][0] == 10 and board[i+1][0] < 10:
                    bonus1 = board[i+1][0]
                    bonus2 = board[i+1][1]
                    score = 10 + bonus1 + bonus2
                elif (board[i][0] + board[i][1]) == 10:
                    bonus1 = board[i+1][0]
                    score = 10 + bonus1 
                else:
                    score = board[i][0] + board[i][1]
                total_score = total_score + score
            print(total_score)
            print(self.score_board)
            return total_score
        except IndexError as e:
            print("Index Error occured in score(): ", str(e))
        except Exception as e:
            print("Error occured in score(): ", str(e))











