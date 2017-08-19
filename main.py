from map.grid import Grid
from map.cell import Cell

if __name__ == "__main__":
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


