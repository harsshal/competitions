# Complete the function below.
# need to traverse all the mappings
# recursive addition

import sys
import os
sys.stdin = open("input")

def  friendCircles(friends):
    # total students = len(friends)
    # while student belongs to a circle(circle_cnt) dont do anything
    # else add(student,list of circles, circle_cnt + 1)
    # inside add, add our students and call add on all his friends
    nStudents = len(friends)
    fCircles = []

    for s in range(nStudents):
        c = checkExistence(s, fCircles)
        if c == -1 :
            fCircles.append([s])
            c = len(fCircles)
            fCircles =  addFriends(s,c-1,fCircles, friends)

    return len(fCircles)


def addFriends(s, c, fCircles, friends):
    for i in range(len(friends[s])):
        if friends[s][i] == 'Y' and i != s and checkExistence(i,fCircles) == -1:
            fCircles[c].append(i)
            addFriends(i,c,fCircles,friends)
    return fCircles


def checkExistence(s,fCircles):
    for c in range(len(fCircles)):
        if s in fCircles[c]:
            return c
    return -1


def main():

    _friends_cnt = int(input())
    _friends_i=0
    _friends = []
    while _friends_i < _friends_cnt:
        _friends_item = input()
        _friends.append(_friends_item)
        _friends_i+=1


    res = friendCircles(_friends);
    print(str(res))

main()
