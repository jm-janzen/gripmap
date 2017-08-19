
class Cell():
    def __init__(self, char, *coords):
        """ Set display character, and (x,y) coordinates

        TODO Accept optional z-axis (or default 0)

        """
        self.char      = char
        self.x, self.y = coords

    def validate(cell):
        """ TODO Validate that object is type of Cell,
        or similar enough to Cell to be cast to one """
        return False

    def __repr__(self):
        """ Return string of members """
        return str(self.__dict__)

class Wall(Cell):
    def __init__(self, *coords):
        Cell.__init__(self, '█', *coords)

class Floor(Cell):
    def __init__(self, *coords):
        Cell.__init__(self, ' ', *coords)

