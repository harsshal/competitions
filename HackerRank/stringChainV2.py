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
    steps = {}

    for curWord in w:
        if curWord not in steps:
            steps[curWord] = 1
        parentList = findParents(curWord, w)
        for parentword in parentList:
            steps[parentword] = steps[curWord] + 1

    return max(steps.values())


def findParents(curWord, w):
    parentList = []
    for word in w:
        if len(word) == len(curWord)+ 1:
            if isParent(curWord,word):
                parentList.append(word)

    return parentList


def isParent(curWord, parent):
    i = j = 0
    while i < len(parent) and j < len(curWord):
        if parent[i] == curWord[j] :
            j += 1
        i += 1

    if i - j > 1:
        return 0
    else:
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