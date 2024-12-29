#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-8.1.txt", 'r') as file:

    grid = [list(line.strip()) for line in file]

    rows = len(grid)
    cols = len(grid[0])
    antinodes = set()

    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(rows):
                for c2 in range(cols):
                    if (r1, c1) != (r2, c2) and grid[r1][c1] == grid[r2][c2] and grid[r1][c1] != '.':
                        dr = r2 - r1
                        dc = c2 - c1

                        r3 = r1 - dr
                        c3 = c1 - dc
                        r4 = r2 + dr
                        c4 = c2 + dc

                        if 0 <= r3 < rows and 0 <= c3 < cols:
                            antinodes.add((r3, c3))
                        if 0 <= r4 < rows and 0 <= c4 < cols:
                            antinodes.add((r4, c4))

    print(len(antinodes))
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-8.2.txt", 'r') as file:
    
    grid = [list(line.strip()) for line in file]

    pass
#--------------------------------------------------------------------------------------------------