from map.cell import Cell, Wall, Floor, Door

class Grid():

    def __init__(self, *dim):
        """ Set member dimensions """
        self.cells = []

        self.width, self.height = dim

        for col in range(self.width):
            for row in range(self.height):
                self.cells.append(Cell('?', col, row))

    @property
    def area(self):
        return self.width * self.height

    def add_cell(self, cell):
        """ Validate and assign Cell at given pos
        
        TODO Accept Cell obj, or anything with appropriate members
        
        """
        x, y = cell.pos
        if x > self.width or y > self.height:
            raise ValueError(f"Cell({cell.x}, {cell.y}) is out of bounds ({self.width}, {self.height})")

        self.cells.append(cell)

    def flood(self, c):
        """ Flood fill all Cells with given character """
        for cell in self.cells:
            cell.char = c

    def _get_cell(self, *pos):
        """ Return cell at given (x,y); yes, hashmap would be better """
        for cell in self.cells:
            if cell.pos == pos:
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

class Room(Grid):

    def __init__(self, *dim):
        """ Init Grid with Wall, Floor Cells """
        Grid.__init__(self, *dim)

        self.doors = []

        # Draw Grid with Wall & Floor Cells
        for row in range(self.height):
            for col in range(self.width):

                if row == 0:                    self.add_cell(Wall(col, row))   # Top
                elif row == self.height - 1:    self.add_cell(Wall(col, row))   # Bottom
                elif col == 0:                  self.add_cell(Wall(col, row))   # Left
                elif col == self.width - 1:     self.add_cell(Wall(col, row))   # Right
                else:                           self.add_cell(Floor(col, row))  # Floor

    def add_door(self, *pos):
        """ Punch hole in a Wall
        
        TODO Validate is actually in a wall.
        
        """

        # Add to list of doors
        self.doors.append(Door(*pos))

        # Add to primitive parent
        self.add_cell(Door(*pos))

