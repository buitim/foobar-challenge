BOARD_SIZE = 8                                                                              # The number of nodes in each row on the boards
ALLOWED_MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]    # List of tuples describing the allowed movements

class Node:
    def __init__(self, x, y):
        # Define coordinates
        self.x = x
        self.y = y
        self.isVisited = False

class Board:
    def __init__(self, size, allowedMoves):
        self.size = size
        self.allowedMoves = allowedMoves
        
        # Create the board
        # Source: https://stackoverflow.com/a/2397150
        self.board = [[-1 for col in range(self.size)] for row in range(self.size)]
        
        # Initialize values on board
        value = 0
        for row in range(self.size):
            for col in range(self.size):
                self.board[row][col] = value
                value += 1
        
        for row in self.board:
            print(row)

    def getCoords(self, position):
        '''
        This takes position and turns it into a tuple of (x, y) coordinates.
        Returns a tuple of (-1, -1) if error / not found
        '''
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == position:
                    return (row, col)
        return (-1, -1)

def solution(src, dest):
    # NOTE: This is a BFS problem (shortest path)
    # TODO: Create the board
    board = Board(BOARD_SIZE, ALLOWED_MOVES)

    # TODO: Set start point

    # TODO: Set destination point

    # TODO: Get the shortest path

solution(0, 30)