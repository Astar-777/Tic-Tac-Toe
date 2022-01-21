import os

class TicTacToe:
    def __init__(self):
        while True:
            self.title = '''
 ▀█▀ █ █▀▀ ▄▄ ▀█▀ ▄▀█ █▀▀ ▄▄ ▀█▀ █▀█ █▀▀
 ░█░ █ █▄▄ ░░ ░█░ █▀█ █▄▄ ░░ ░█░ █▄█ ██▄
-----------------------------------------
            '''
            self.start()
            print()
            choice=input('Do you want to play again? (Y/N): ').upper()
            os.system("cls" if os.name == 'nt' else 'clear')
            if choice=='N':
                print('OK')
                break


    def make_board(self):
        return [x for x in range(9)]
        
        
    def print_board(self, board):
        for i in range(0, 7, 3): 
            for j in board[i:i+3]:
                print(j,end= '    ')
            print('\n')


    def move(self, letter, pos, board):
        board[pos] = letter


    def free(self, pos, board):
        return board[pos]==pos 


    def full(self, board):
        for i in board:
            if type(i) == int:
                return False
        return True


    def chance(self, letter, board):
        while True:
            try:
                pos = int(input(f'Enter a position for \'{letter}\': '))
            except:
                continue
            try:
                assert pos in range(9)
            except AssertionError:
                print('Invalid position! Try Again!')
                continue
            if self.free(pos, board):
                self.move(letter, pos, board)
                break
            else:
                print('Position already occupied!')


    def vertical_win(self, board):
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6]:
                return board[i]


    def horizontal_win(self, board):
        for i in range(0,7,3):
            if board[i]==board[i+1]==board[i+2]:
                return board[i]


    def diagonal_win(self, board):
        if board[0]==board[4]==board[8]:
            return board[0]
        if board[2]==board[4]==board[6]:
            return board[2]


    def winner(self, board):
        if _ := self.vertical_win(board):
            return _
        if _ := self.horizontal_win(board):
            return _
        if _ := self.diagonal_win(board):
            return _
        return None


    def start(self):
        print(self.title)

        board = self.make_board()
        self.print_board(board)
        while not self.full(board) and not self.winner(board):
            self.chance('X', board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.title)
            self.print_board(board)
            if self.full(board) or self.winner(board):
                break

            self.chance('O', board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.title)
            self.print_board(board)

        if self.winner(board):
            print(f'\'{self.winner(board)}\' wins!')

        if self.full(board):
            print('Tie!')


TicTacToe()