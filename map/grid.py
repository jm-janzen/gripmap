from map.cell import Cell

class Grid():

    cells = []

    def __init__(self, *dim):
        """ Set member dimensions """
        self.width, self.height = dim

    def add_cell(self, cell):
        """ Validate and assign Cell at given coords """
        if cell.x > self.width or cell.y > self.height:
            raise ValueError(f"Cell({cell.x}, {cell.y}) is out of bounds ({self.width}, {self.height})")

        self.cells.append(cell)

    def _get_cell(self, *coords):
        """ Return cell at given (x,y); yes, hashmap would be better """
        for cell in self.cells:
            if (cell.x, cell.y) == coords:
                ret = cell
        return ret

    def __repr__(self):
        """ Return string of members """
        return str(self.__dict__)

    def __str__(self):
        """ Return grid string

        TODO Optimise

        """
        ret = ''
        for col in range(self.width):
            for row in range(self.height):
                ret += self._get_cell(col, row).char
            ret += '\n'
        return ret

if __name__ == "__main__":
    g = Grid(2,2)
    print(str(g))
