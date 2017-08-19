
def main():
    test_str = ""     \
            + "oox\n" \
            + "oxo\n" \
            + "xoo\n"

    # Build grid actual
    grid  = Grid(3, 3)

    for col in range(grid.width):
        for row in range(grid.height):

            char = 'o'
            if   (col, row) == (0,2): char = 'x'
            elif (col, row) == (1,1): char = 'x'
            elif (col, row) == (2,0): char = 'x'

            grid.add_cell(Cell(char, col, row))

    actual_str = str(grid)


    print(f"Test:\n{test_str}")
    print(f"Actual:\n{actual_str}")

    try:
        assert (test_str == actual_str), "Test Failed!"
    except AssertionError as e:
        print(e)
    else:
        print("Test Passed!")


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

if __name__ == "__main__": main()

