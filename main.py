from map.grid import Room
from map.cell import Cell
from map.map  import Map

if __name__ == "__main__":

    """
    r = Room(12, 24)

    r.add_door(0,3)

    print("Room members:", repr(r))
    print(r)
    """

    m = Map(3, 50, 50)

    #print("Map members:", repr(m))
    for i, r in enumerate(m.rooms):
        print(f"Room #{i} ({r.width}*{r.height})\n{r}")

    print(repr(m))

    print(m)

