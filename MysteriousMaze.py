import sys

def search(maze, size, start, end):
    searching = [[start]]
    while len(searching[len(searching)-1]) > 0:
        next_round = []
        for point in searching[len(searching)-1]:
            if point[0] < size-1 and maze[point[0]+1][point[1]] == 1:
                next_round.append([point[0]+1, point[1]])
            if point[1] > 0 and maze[point[0]][point[1]-1] == 1:
                next_round.append([point[0],point[1]-1])
            if point[1] < size-1 and maze[point[0]][point[1]+1] == 1:
                next_round.append([point[0],point[1]+1])
        for point in next_round:
            item = next((item for item in searching[len(searching)-1] if point[0] == item[0] and point[1] == item[1]), None)
            if item != None:
                next_round.remove(item)
            if point[0] == end[0] and point[1] == end[1]:
                return True
        searching.append(next_round)
    return False

#All Stdin at once!
input_data = sys.stdin.readlines()

maze_size = int(input_data.pop(0))

maze = [[0 for y in range(maze_size)] for x in range(maze_size)]
maze_open = False

doors = 0
while not maze_open:
    door = [int(c) for c in input_data.pop(0).split()]
    if len(door) == 2:
        maze[door[0]-1][door[1]-1] = 1
        doors = doors+1
    else:
        print -1
        break
    # Path Finding
    for a in range(maze_size):
        if maze[0][a] == 1:
            for z in range(maze_size):
                if maze[maze_size-1][z] == 1:
                    if search(maze, maze_size, [0,a], [maze_size-1,z]):
                        print doors
                        exit()
