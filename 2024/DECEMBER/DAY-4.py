#--------------------------------------------------------------------------------------------------
#PART - ONE
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-4.1.txt", 'r') as inputs:

    inputs = inputs.read()
    grid = inputs.split()

    def find_word(grid):
        row = len(grid)
        col = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (0, -1), (1, -1)]
        word = "XMAS"
        count = 0
        
        for x in range(row):
            for y in range(col):
                for dx, dy in directions:
                    if define_word(grid, x, y, word, dx, dy):
                        count += 1
        return count

    def define_word(grid, x, y, word, dx, dy):
        row, col = len(grid), len(grid[0])
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not ( 0 <= nx < row and 0 <= ny < col):
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    print(f"PART - ONE : {find_word(grid)}") 
#--------------------------------------------------------------------------------------------------
#PART - TWO
#--------------------------------------------------------------------------------------------------
with open("2024/DEC-INPUTS/DEC-DAY-4.2.txt", 'r') as inputs2:
    
    grid2 = inputs2.read().split()

    rows = len(grid2)
    cols = len(grid2[0])
    count2 = 0

    for x in range(rows):
        for y in range(cols):
            if grid2[x][y] == 'A':
                if (0 <= x + 1 < rows and 0 <= x - 1 < rows and 
                    0 <= y + 1 < cols and 0 <= y - 1 < cols):
                    diag_m = grid2[x-1][y-1] + grid2[x][y] + grid2[x+1][y+1]
                    diag_s = grid2[x-1][y+1] + grid2[x][y] + grid2[x+1][y-1]
                    if ((diag_m == 'MAS' or diag_m == 'SAM') and 
                    (diag_s == 'MAS' or diag_s == 'SAM')):
                        count2 += 1

    print("PART - TWO : " + str(count2))
#--------------------------------------------------------------------------------------------------