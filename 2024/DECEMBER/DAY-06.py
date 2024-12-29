#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-6.1.txt", 'r') as inputs:

    grid = inputs.read().split()
    grid = [list(row) for row in grid]

    rows = len(grid)
    cols = len(grid[0])
    x, y = 0, 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                x, y = i, j

    out = False
    directions = ["^", ">", "v", "<"] 
    current_dir = "^"
    res = 0

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def turn_right(curr_dir):
        idx = directions.index(curr_dir)
        return directions[(idx + 1) % len(directions)]

    while out == False:

        if current_dir == "^":
            if is_in_bounds(x - 1, y):
                if grid[x - 1][y] != "#":
                    grid[x][y] = "X"
                    x, y = x - 1, y
                else:
                    current_dir = turn_right(current_dir)
            else:
                out = True
                break
        elif current_dir == ">":
            if is_in_bounds(x, y + 1):
                if grid[x][y + 1] != "#":
                    grid[x][y] = "X"
                    x, y = x, y + 1
                else:
                    current_dir = turn_right(current_dir)
            else: 
                out = True
                break
        elif current_dir == "v":
            if is_in_bounds(x + 1, y): 
                if grid[x + 1][y] != "#":
                    grid[x][y] = "X"
                    x, y = x + 1, y
                else:
                    current_dir = turn_right(current_dir)
            else:
                out = True
                break
        elif current_dir == "<":
            if is_in_bounds(x, y - 1): 
                if grid[x][y - 1] != "#":
                    grid[x][y] = "X"
                    x, y = x, y - 1
                else:
                    current_dir = turn_right(current_dir)
            else:
                out = True
                break

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                res += 1

    print("Number:", res + 1)
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
pass
#--------------------------------------------------------------------------------------------------