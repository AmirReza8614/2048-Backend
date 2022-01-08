import random

class Game:
    ## Init
    def __init__(self):
        ## Empty board
        self._board = []
        for counter in range(4):
            self._board.append([0]*4)

        ## Add 2 item for start
        self._board = self.__append_number(self._board)
        self._board = self.__append_number(self._board)


    ## Central Commands    
    def move(self, string = None):
        boards = self._board.copy()
        var = str(boards)
        if string == "right":
            boards = self.__positive_command(boards)
            
        elif string == "left":
            boards = self.__negative_command(boards)
            
        elif string == "up":
            boards = self.__reverse_command(boards)
            
            boards = self.__negative_command(boards)

            boards = self.__reverse_command(boards)

        elif string == "down":
            boards = self.__reverse_command(boards)

            boards = self.__positive_command(boards)

            boards = self.__reverse_command(boards)

        else:
            return print("Unknown input")
        
        if str(boards) != var:
            self._board = self.__append_number(boards)

    def is_game_finished(self):
        boards = self._board
        finish = True
        for board in boards:
            if board.count(0) != 0:
                finish = False
        return finish

    def get_board(self):
        return self._board


        ## Subcommands
    def __append_number(self, boards):
        loop = not self.is_game_finished()

        while loop:
            arandom = random.randint(0, 3)
            brandom = random.randint(0, 3)
            if boards[arandom][brandom] == 0:
                boards[arandom][brandom]=random.choices([2,4], weights = [5, 1])[0]
                loop = False
        return boards

    def __positive_command(self, boards):
        for jcounter, board in enumerate(boards):
            for icounter, item in enumerate(board):
                if item == 0:
                    boards[jcounter].pop(icounter)
                    boards[jcounter].insert(0, 0)

            for icounter in range(3):
                if board[icounter] == board[icounter+1] and board[icounter] > 0:
                    board[icounter+1] = (board[icounter+1] + board[icounter]) * -1
                    board[icounter] = 0

            for icounter in range(4):
                if board[icounter] < 0:
                    board[icounter] = board[icounter] * -1

            for icounter, item in enumerate(board):
                if item == 0:
                    boards[jcounter].pop(icounter)
                    boards[jcounter].insert(0, 0)

        return boards

    def __negative_command(self, boards):
        for jcounter, board in enumerate(boards):
            for icounter, item in enumerate(board):
                if item == 0:
                    boards[jcounter].pop(icounter)
                    boards[jcounter].append(0)

            for icounter in range(3, 0, -1):
                if board[icounter] == board[icounter-1] and board[icounter] > 0:
                    board[icounter-1] = (board[icounter-1] + board[icounter]) * -1
                    board[icounter] = 0

            for icounter in range(4):
                if board[icounter] < 0:
                    board[icounter] = board[icounter] * -1

            for icounter, item in enumerate(board):
                if item == 0:
                    boards[jcounter].pop(icounter)
                    boards[jcounter].append(0)

        return boards

    def __reverse_command(self, boards1):
        boards = [[],[],[],[]]
        for board in boards1:
            for counter, item in enumerate(board):
                boards[counter].append(item)

        return boards
