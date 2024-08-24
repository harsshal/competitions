__author__ = 'harsshal'
# need to write def newLocation(i,j,M,N)
# if in north
#     move_left
# in west
#     move down
# in south
#     move right
# in east
#     move up
# diagonal elements are the place where we change format

#!/bin/python3

import math
import sys
sys.stdin = open("input")


def newLocation(R,C,r,c):
    # if element belongs to north, move left
    if(r+c < C and r<min(R,C)/2 and r < c ):
        c -= 1
    # if element belongs to west, move down
    elif(r >= c and c<min(R,C)/2 and c+r<R-1):
        r += 1
    # if element belongs to south, move right
    elif(r+c >= R-1 and r >= R-(min(R,C)/2) and r - c > R-C ):
        c += 1
    # if element belongs to east, move up
    elif(r - c <= R-C and c >= C-(min(R,C)/2) and r+c>=C):
        r -= 1
    return [r,c]


def main():
    R, C, S = input().strip().split(' ')
    R, C, S = [int(R), int(C), int(S)]
    G = [[int(num) for num in input().strip().split(' ')] for line in range(R)]
    newG = [[0 for num in range(C)] for row in range(R)]
    list=[[] for l in range(math.floor(min(R,C)/2))]
    for l in range(math.floor(min(R,C)/2)):
        [r,c] = [l,l]
        [newR,newC] = [-1,-1]
        while newR!=l or newC!=l:
            [newR,newC] = newLocation(R,C,r,c)
            list[l].append([newR,newC])
            [r,c] = [newR,newC]
    for r in range(R):
        for c in range(C):
            for l in range(math.floor(min(R,C)/2)):
                if [r,c] in list[l]:
                    loc = list[l].index([r,c])
                    loc = (loc + S)%len(list[l])
                    [newR,newC] =  list[l][loc]
                    newG[newR][newC] = G[r][c]
    #print(len(list),len(list[1]))
    for r in range(R):
        print(' '.join(map(str,newG[r][:])))


main()
