
class Cell:

    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        neighbors = []
        if x > 0:
            neighbors.append( (x-1, y) )
        if x < max_x:
            neighbors.append( (x+1, y) )
        if y > 0:
            neighbors.append( (x, y-1) )
        if y < max_y:
            neighbors.append( (x, y+1) )
                
    def get_neighbors(self):
        return neighbors
