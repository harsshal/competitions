__author__ = 'harsshal'

import sys
import os
sys.stdin = open("input")

# Complete the function below.
# idea 1 : create lists [[bigger word, smaller word, small word]]
# add rest of smaller word in the list. need to keep count of max chain till that word
# is the input sorted by length?
# idea 2 : we can start with a = 1 , get all possible guys which have a aas substring and then assign them 2. from n char string, to n-1 start matching, only one skip in n+1 is allowed and then we should match.
# list of lists 'strlen' to keep input sorted
# dictionary 'steps' to keep max steps for a word


def longest_chain( w):
    strlen = [[] for len in range(51)]
    steps = {}

    # max length will be 50 so should be OK.
    for curWord in w:
        curLen = len(curWord)
        if len(strlen[curLen]) == 0:
            strlen[len(curWord)] = [curWord]
        else:
            strlen[len(curWord)].append(curWord)

    for i in range(51):
        if len(strlen[i]) != 0:
            for curWord in strlen[i]:
                if curWord not in steps:
                    steps[curWord] = 1
                parentList = findParents(curWord, strlen)
                for parentword in parentList:
                    steps[parentword] = steps[curWord] + 1

    return max(steps.values())


def findParents(curWord, strlen):
    if len(strlen[len(curWord)+1]) == 0:
        return []
    else:
        parentList = []
        for parent in strlen[len(curWord)+1]:
            if isParent(curWord,parent):
                parentList.append(parent)
        return parentList


def isParent(curWord, parent):
    j = 0
    for i in range(len(parent)):
        # we can skip only 1 leter. Rest should match
        if ( i - j > 1):
            return 0
        if len(curWord) > j and parent[i] == curWord[j]:
            j += 1
    return 1

def main():
    _w_cnt = 0
    _w_cnt = int(input())
    _w_i=0
    _w = []
    while _w_i < _w_cnt:
        _w_item = input()
        _w.append(_w_item)
        _w_i+=1


    res = longest_chain(_w);
    print(str(res))


main()