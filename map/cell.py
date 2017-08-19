
class Cell():
    def __init__(self, char, *coords):
        """ Set display character, and (x,y) coordinates

        TODO Accept optional z-axis (or default 0)

        """
        self.char      = char
        self.x, self.y = coords

    def __repr__(self):
        """ Return string of members """
        return str(self.__dict__)

