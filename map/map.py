from map.grid import Grid, Room
from map.cell import Cell

import random

class Map(Grid):

    def __init__(self, num_rooms, *dim):

        Grid.__init__(self, *dim)

        self.rooms      = []
        self.area_avail = self.area

        # TODO Figure out how to fit
        #      num_rooms in area of dim.
        #      Will need pos, to prevent overlapping
        room_height_min = 9
        room_width_min  = 9

        for i in range(num_rooms):

            tmp_room_width  = Utils.clamp(random.randint(room_width_min, int(self.width / num_rooms)),
                                          self.width)
            tmp_room_height = Utils.clamp(random.randint(room_height_min, int(self.height / num_rooms)),
                                          self.height)

            tmp_room_pos    = (0,0)

            # TODO Figure out position of rooms so they don't overlap
            tmp_room_cls = MapRoom(tmp_room_pos, tmp_room_width, tmp_room_height)
            tmp_room_cls.flood(str(i))

            self.rooms.append(tmp_room_cls)

        # TODO Populate cells with chars from rooms @ given positions
        #      Should be easy using pos of ea room as offsets
        for col in range(self.width):
            for row in range(self.height):

                """
                for r in self.rooms:
                    print("R:", repr(r))
                x = (col, row)
                y = [room["cells"] for room in self.rooms]
                self.add_cell(Cell('o', col, row))
                """
                pass

    def __str__(self):
        """ Return map string """
        ret = ''
        print(self.width, self.height)
        for col in range(self.width):
            for row in range(self.height):
                ret += self._get_cell(col, row).char
            ret += '\n'

        return ret

    def __repr__(self):
        """ Return string summary of members """
        tmp_dict = {}
        for k, v in self.__dict__.items():
            # Only return number of rooms to prevent terminal spam
            if k == "rooms" or k == "cells":
                tmp_dict["num_"+k] = len(v)
            else:
                tmp_dict[k] = v
        return str(tmp_dict)

class MapRoom(Room):

    def __init__(self, pos, *dim):
        """ Init Room at coordinates (top-left), using given dimensions """
        Room.__init__(self, *dim)
        self.pos = pos

class Utils():
    def clamp(n, maximum, minimum=0):
        ret = max(minimum, min(n, maximum))
        #print(f"clamp({n}, {maximum}, {minimum}) => {ret}")
        return ret

