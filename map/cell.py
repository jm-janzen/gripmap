
class Cell():
    def __init__(self, char, *pos):
        """ Set display character, and (x,y) coordinates

        TODO Accept optional z-axis (or default 0)

        """
        self.char      = char
        self.pos       = pos

    def validate(cell):
        """ TODO Validate that object is type of Cell,
        or similar enough to Cell to be cast to one """
        return False

    def __repr__(self):
        """ Return string of members """
        return str(self.__dict__)

class Wall(Cell):
    def __init__(self, *pos):
        Cell.__init__(self, '█', *pos)

class Floor(Cell):
    def __init__(self, *pos):
        Cell.__init__(self, ' ', *pos)

class Door(Cell):
    def __init__(self, *pos):
        Cell.__init__(self, '+', *pos)

