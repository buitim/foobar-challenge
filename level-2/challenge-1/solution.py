BOARD_SIZE = 8                                                                              # The number of nodes in each row on the boards
ALLOWED_MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]    # List of tuples describing the allowed movements

class Node:
    def __init__(self, x, y, distance = 0):
        # Define coordinates
        self.x = x
        self.y = y
        self.distance = distance
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
        
def navigate(src, dest):
    # Source: https://docs.python.org/3/library/collections.html#collections.deque
    queue =[]                                   # Create a new empty queue
    queue.append(src)                           # Add the starting point to the queue

    # Start the BFS portion
    while queue:
        # Dequeue
        currNode = queue.pop(0)                 # Pop the front of the queue
        currDistance = currNode.distance
        x = currNode.x
        y = currNode.y

        # Check if destination
        if (currNode.x == dest.x and currNode.y == dest.y):
            return currDistance

        # Check visited
        if not currNode.isVisited:
            currNode.isVisited = True            # First, mark the node as visited

            # Now we check all of the moves.
            for i in range(len(ALLOWED_MOVES)):
                (nextX, nextY) = tuple(map(lambda i, j: i + j, (x, y), ALLOWED_MOVES[i]))
                
                # Then, we check if new coordinates are valid (i.e. on the board)
                if (nextX >= 0 and nextX <= BOARD_SIZE and nextY >= 0 and nextY <= BOARD_SIZE):
                    # If it is, queue up the next node and increment the distance
                    nextNode = Node(nextX, nextY, currDistance + 1)
                    queue.append(nextNode)

    return -1

def solution(src, dest):
    '''
    NOTE: This is a BFS problem (shortest path)
    Helpful source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    '''
    # Create the board
    board = Board(BOARD_SIZE, ALLOWED_MOVES)

    # Set start point
    (startX, startY) = board.getCoords(src)
    startNode = Node(startX, startY)

    # Set destination point
    (endX, endY) = board.getCoords(dest)
    endNode = Node(endX, endY)

    # Go time
    return navigate(startNode, endNode)