from random import randint
from random import shuffle


def build_maze(m, n, swag):
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append("wall")
        grid.append(row)
    start_i = randint(0, m - 1)
    start_j = randint(0, n - 1)
    grid[start_i][start_j] = 'Start'
    mow(grid, start_i, start_j)
    i, j = explore_maze(grid, start_i, start_j, swag)
    print_maze(grid)
    print('\n'+ "DFS benutzt")
    mace_windo, collector = dfs(grid, start_i, start_j, i, j)
    grid[start_i][start_j] = 'Start'  # Um Den Startpunkt zu markieren
    print_maze(mace_windo, collector)
    print("Der * markiert die gelaufenen Schritte" )


def print_maze(grid, collector=None): # Hab mich entschieden den Sammler direkt hier zu machen.
    for row in grid:
        printable_row = ''
        for cell in row:
            if cell == 'wall':
                char = '|'
            elif cell == 'empty':
                char = ' '
            elif cell == 'traveled':
                char = '*'
            else:
                char = cell[0]
            printable_row += char
        print(printable_row)
    if collector:
        first = list(set(collector))
        for collection in first:
            count = collector.count(collection)
            print('Du hast {0}x {1} gesammelt.'.format(count, collection))


def mow(grid, i, j):
    directions = ['U', 'D', 'L', 'R']
    while len(directions) > 0:
        directions_index = randint(0, len(directions) - 1)
        direction = directions.pop(directions_index)
        if direction == 'U':
            if i - 2 < 1:
                continue
            elif grid[i - 2][j] == 'wall':
                grid[i - 1][j] = 'empty'
                grid[i - 2][j] = 'empty'
                mow(grid, i - 2, j)
        elif direction == 'D':
            if i + 2 >= len(grid) - 1:
                continue
            elif grid[i + 2][j] == 'wall':
                grid[i + 1][j] = 'empty'
                grid[i + 2][j] = 'empty'
                mow(grid, i + 2, j)
        elif direction == 'L':
            if j - 2 < 1:
                continue
            elif grid[i][j - 2] == 'wall':
                grid[i][j - 1] = 'empty'
                grid[i][j - 2] = 'empty'
                mow(grid, i, j - 2)
        else:
            if j + 2 >= len(grid[0]) - 1:
                continue
            elif grid[i][j + 2] == 'wall':
                grid[i][j + 1] = 'empty'
                grid[i][j + 2] = 'empty'
                mow(grid, i, j + 2)


def explore_maze(grid, start_i, start_j, swag):
    grid_copy = [row[:] for row in grid]
    bfs_queue = [[start_i, start_j]]
    directions = ['U', 'D', 'L', 'R']
    while bfs_queue:
        i, j = bfs_queue.pop(0)
        if grid[i][j] != 'Start' and randint(1, 10) == 1:
            grid[i][j] = swag[randint(0, len(swag) - 1)]
        grid_copy[i][j] = 'visited'
        for direction in directions:
            explore_i = i
            explore_j = j
            if direction == 'U':
                explore_i = i - 1
                if explore_i < 0:
                    continue
                elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                    bfs_queue.append([explore_i, explore_j])
            elif direction == 'D':
                explore_i = i + 1
                if explore_i >= len(grid):
                    continue
                elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                    bfs_queue.append([explore_i, explore_j])
            elif direction == 'L':
                explore_j = j - 1
                if explore_j < 0:
                    continue
                elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                    bfs_queue.append([explore_i, explore_j])
            else:
                explore_j = j + 1
                if explore_j >= len(grid[0]):
                    continue
                elif grid_copy[explore_i][explore_j] != 'visited' and grid_copy[explore_i][explore_j] != 'wall':
                    bfs_queue.append([explore_i, explore_j])
    grid[i][j] = 'End'
    return i, j


def dfs(grid, start_i, start_j, end_i, end_j, visited=None, collector=None):
    current_vertex = '{0},{1}'.format(start_i, start_j)
    current_vertex = 'Start'
    current_vertex = '{0},{1}'.format(start_i, start_j)
    target_vertex = '{0},{1}'.format(end_i, end_j)
    if visited is None:
        visited = []
    visited.append(current_vertex)
    if current_vertex == target_vertex:
        return grid, collector

    neighbors = []
    directions = ['U', 'D', 'L', 'R']
    shuffle(directions)
    if collector is None:
        collector = []
    if grid[start_i][start_j] != 'empty' and grid[start_i][start_j] != 'Start':
        collector.append(grid[start_i][start_j])
    grid[start_i][start_j] = 'traveled'
    for direction in directions:
        explore_i, explore_j = start_i, start_j
        if direction == 'U':
            if explore_i - 1 < 0:
                continue
            elif grid[explore_i - 1][explore_j] != 'wall' and grid[explore_i - 1][explore_j] != 'traveled':
                neighbor = '{0},{1}'.format(explore_i - 1, explore_j)
                neighbors.append(neighbor)
        elif direction == 'D':
            if explore_i + 1 >= len(grid):
                continue
            elif grid[explore_i + 1][explore_j] != 'wall' and grid[explore_i + 1][explore_j] != 'traveled':
                neighbor = '{0},{1}'.format(explore_i + 1, explore_j)
                neighbors.append(neighbor)
        elif direction == 'L':
            if explore_j - 1 < 0:
                continue
            elif grid[explore_i][explore_j - 1] != 'wall' and grid[explore_i][explore_j - 1] != 'traveled':
                neighbor = '{0},{1}'.format(explore_i, explore_j - 1)
                neighbors.append(neighbor)
        elif direction == 'R':
            if explore_j + 1 >= len(grid[0]):
                continue
            elif grid[explore_i][explore_j + 1] != 'wall' and grid[explore_i][explore_j + 1] != 'traveled':
                neighbor = '{0},{1}'.format(explore_i, explore_j + 1)
                neighbors.append(neighbor)

    for neighbor in neighbors:
        if neighbor not in visited:
            neighbor = neighbor.split(',')
            start_i, start_j = int(neighbor[0]), int(neighbor[1])
            path = dfs(grid, start_i, start_j, end_i, end_j, visited, collector)
            if path:
                return path


build_maze(20, 50, ['candy corn', 'werewolf', 'pumpkin'])
