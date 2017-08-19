from map.grid import Room
from map.cell import Cell

if __name__ == "__main__":

    r = Room(12, 12)

    r.add_door(0,3)

    print(repr(r))
    print(r)


