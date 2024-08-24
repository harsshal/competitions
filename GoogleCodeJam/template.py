import fileinput

def raw_input():
    print("raw input")
    
def solve():
    print("solve")


def read_input():
    import sys
    with sys.stdin as file:
        nTests = int(file.readline())
        for test in range (1, nTests+1):
            print(test)
            

read_input()