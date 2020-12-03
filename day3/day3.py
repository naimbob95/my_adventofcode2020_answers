import os 
from random import sample


def readfromtxt():
    files = open('input.txt', 'r') 
    all_trails = []
    for line in files:
        # trails = []
        all_trails.append(line.rstrip())
        # all_trails.append(trails)
        
    files.close()    
    return all_trails


def findthetreesdown1(value,trails):
    slop_right = value
    # slop_down = 1
    pos = -value 
    trees = 0
    for t in trails: 
        # print(t[0])
            pos = pos + slop_right 
            if  pos < 31: 
                # print(t[pos])
                # print(t[pos])
                if t[pos] == "#":
                    trees += 1
                else:
                    continue
            else:
                pos = pos - 31
                # print(pos)
                if t[pos] == "#":
                    trees += 1
                else:
                    continue
    return trees

##should improve this one make more dynamic function
def findthetreesdown2(value,trails):
    slop_right = value
    # slop_down = 1
    pos = -value
    trees = 0
    i = -1
    for t in trails:
        i += 1
        if (i % 2) == 0:
            pos = pos + slop_right 
            # print("Even")
            if  pos < 31: 
                if t[pos] == "#":
                    trees += 1
                else:
                    continue
            else:
                pos = pos - 31
                if t[pos] == "#":
                    trees += 1
                else:
                    continue
        else:
            continue
            # print("Odd")
        # print(t[0])
    return trees

def main():
    trails = readfromtxt()
    # print(trails)
    
    slope1 = findthetreesdown1(1,trails)
    slope2 = findthetreesdown1(3,trails)
    slope3 = findthetreesdown1(5,trails)
    slope4 = findthetreesdown1(7,trails)
    slope5 = findthetreesdown2(1,trails)
    # print(slope5)
    result = slope1 * slope2 * slope3 * slope4 * slope5
    print("The answer for Part1: "+str(slope2))
    print("The answer for Part2: "+str(result))
    # slope5 = findthetrees2(value,trails)
    # print(tree)
if __name__ == "__main__":
    main()