MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, x, y, blocked = False):
        # Define coordinates
        self.x = x
        self.y = y
        self.distance = 1
        self.isBlocked = blocked
        self.isVisited = False

class Board:
    def __init__(self, board):
        self.board = board
        self.shortestDistance = -1
        self.width = len(board[0])
        self.height = len(board)
        self.canRemove = True

    def checkWall(self, x, y):
        '''
        Returns True if the location is a wall.
        False otherwise
        '''
        return self.board[x][y] == 1

    def getNeighbors(self, node):
        '''
        Returns an array of Nodes
        '''
        neighbors = []
        (x, y) = (node.x, node.y)

        for i in range(len(MOVES)):
            (moveX, moveY) = MOVES[i]
            newX = x + moveX
            newY = y + moveY

            # print(newX, newY)

            # Check for bounds
            if ((newX >= 0 and newX < self.width) and (newY >= 0 and newY < self.height)):
                # print('[=] Within bounds')
                print(self.checkWall(newX, newY))
                neighborNode = Node(newX, newY, self.checkWall(newX, newY))
                
                # Check blocked
                if neighborNode.isBlocked:
                    if self.canRemove:
                        self.canRemove = False
                        neighbors.append(neighborNode)
                else:
                    neighbors.append(neighborNode)
        
        return neighbors

        
    def navigate(self, start):
        queue = []                                  # Create a new empty queue
        queue.append(start)                         # Add the starting point to the queue

        # Start the BFS portion
        while queue:
            # Dequeue
            currNode = queue.pop(0)                 # Pop the front of the queue
            currDistance = currNode.distance
            x = currNode.x
            y = currNode.y
            currNode.isVisited = True               # First, mark the node as visited

            # print('[=] Distance: {}'.format(currDistance))

            # Check if destination
            if (currNode.x == self.width - 1 and currNode.y == self.height - 1):
                # print('[=] At destination')
                return currDistance

            # Check neighbors
            neighborNodes = self.getNeighbors(currNode)
            for node in neighborNodes:
                # Check if visited
                if not node.isVisited:
                    node.distance = currDistance + 1
                    # print('[=] Incremented Distance')
                    queue.append(node)

        return -1

def solution(map):
    '''
    NOTE: This is a BFS problem (shortest path)
    Helpful source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    '''
    board = Board(map)                                          # Create the board

    startNode = Node(0, 0)                                      # Set start point
    # endNode = Node(board.width - 1, board.height - 1)           # Set destination point

    # Go time
    res = board.navigate(startNode)
    # print(res)
    return res