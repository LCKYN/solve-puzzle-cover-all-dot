import numpy as np
import pygame, sys
from pygame.locals import *

import time

start = 10
end = 13
count = 0

res = list()
reject = list()

matrix = np.loadtxt('q.txt',dtype=np.int8)
s = matrix.shape
size = 700
r = np.array([700,700])/s
ga = dict()

for y in range(matrix.shape[0]):
    for x in range(matrix.shape[1]):
        ga[x+y*s[1]] = set()
        if(matrix[y,x]):
            count += 1
            if(x - 1 >= 0 and matrix[y,x-1]):
                tx = x - 1
                ga[x+y*s[1]].add(tx+y*s[1])
            if(y - 1 >= 0 and matrix[y-1,x]):
                ty = y - 1
                ga[x+y*s[1]].add(x+ty*s[1])
            if(x + 1 < s[1] and matrix[y,x+1]):
                tx = x + 1
                ga[x+y*s[1]].add(tx+y*s[1])
            if(y + 1 < s[1] and matrix[y+1,x]):
                ty = y + 1
                ga[x+y*s[1]].add(x+ty*s[1])

def backtracking(path):
    if(len(path) == count and path[-1] == end):
        res.append(path)
    else:
        for adj in ga[path[-1]]:
            if(not adj in path):
                backtracking(path + [adj])
            else:
                reject.append(path)

backtracking([start])

print(res)
fcount = 0

pygame.init()
scr = pygame.display.set_mode((size, size))
pygame.display.set_caption('solver')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for i in ga.keys():
        if(ga[i]):
            x = i % 8
            y = i // 8
            for j in ga[i]:
                x2 = j % 8
                y2 = j // 8
                pygame.draw.line(scr, (20,20,20), \
                                    (x*r[1] + r[1] / 2, y*r[0]  + r[0] / 2), \
                                    (x2*r[1] + r[1] / 2, y2*r[0]  + r[0] / 2), 6)

    if(fcount+1 > len(reject)):
        for i in res:
            for p in range(len(i) - 1):
                x = i[p] % 8
                y = i[p] // 8
                x2 = i[p+1] % 8
                y2 = i[p+1] // 8
                pygame.draw.line(scr, (0,150,0), \
                    (x*r[1] + r[1] / 2, y*r[0]  + r[0] / 2), \
                    (x2*r[1] + r[1] / 2, y2*r[0]  + r[0] / 2), 6)
    else:
        i = reject[fcount]
        for p in range(len(i) - 1):
            x = i[p] % 8
            y = i[p] // 8
            x2 = i[p+1] % 8
            y2 = i[p+1] // 8
            pygame.draw.line(scr, (150,0,0), \
                (x*r[1] + r[1] / 2, y*r[0]  + r[0] / 2), \
                (x2*r[1] + r[1] / 2, y2*r[0]  + r[0] / 2), 6)

    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            if(matrix[y,x]):
                pygame.draw.circle(scr, (255, 255, 255), (x*r[1] + r[1] / 2, y*r[0]  + r[0] / 2), 10)

    fcount += 1
    pygame.display.update()
    time.sleep(0.002)