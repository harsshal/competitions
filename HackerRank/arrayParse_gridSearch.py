__author__ = 'harsshal'

#!/bin/python3

import sys

def matchGrid(G,P,Gr,Gc,r,c):
    match = 1
    for i in range(r):
        for j in range(c):
            if(G[Gr+i][Gc+j]!=P[i][j]):
                match=0
                break
        if(match==0):
            break
    return match


sys.stdin = open("input")

t =int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = [[ int(num) for num in str(input().strip())] for line in range(R)]
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = [[ int(num) for num in str(input().strip())] for line in range(r)]
    found = 0
    for Gr in range(R):
        if(R-Gr < r):
            break
        for Gc in range(C):
            if(C-Gc < c):
                break
            if(matchGrid(G,P,Gr,Gc,r,c)):
                found = 1
                break
        if(found==1):
            break
    if(found==1):
        print("YES")
    else:
        print("NO")