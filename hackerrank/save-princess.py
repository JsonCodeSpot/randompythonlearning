#!/usr/bin/python

def direction(x, y):
    v = 0
    [print(x) for v in y]


def displayPathtoPrincess(n, grid):
    mario_loc = {"col": 0, "row": 0}
    princess_loc = {"col": 0, "row": 0}
    for index, value in enumerate(grid):
        if 'm' in value:
            mario_loc['col'] = value.index('m')
            mario_loc['row'] = index
        if 'p' in value:
            princess_loc['col'] = value.index('p')
            princess_loc['row'] = index
    # direction =
    direction("RIGHT", range(princess_loc['col'] - mario_loc['col']))
    direction("LEFT", range(mario_loc['col'] - princess_loc['col']))
    direction("DOWN", range(princess_loc['row'] - mario_loc['row']))
    direction("UP", range(mario_loc['row'] - princess_loc['row']))


# print all the moves here

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
