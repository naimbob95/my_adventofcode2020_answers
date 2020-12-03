import os 
from random import sample


def readfromtxt():
    files = open('input.txt', 'r') 
    all_trails = []
    for line in files:
        ##append all the string to an array
        all_trails.append(line.rstrip())
        
    files.close()    
    return all_trails


def findthetreesdown1(value,trails):
    slop_right = value
    pos = -value ##this is to get make sure first position of string start with 0
    trees = 0
    for t in trails: 
            
            pos = pos + slop_right  #get the current position of the trails
            if  pos < 31:    ##check if the the postion of string trails is bigger than the max size (31)            
                if t[pos] == "#":  ## if found the '#' in the string, add trees variables to 1
                    trees += 1
                else:
                    continue
            else:
                pos = pos - 31  ##get the current position when the postion is bigger than max size (31)
                if t[pos] == "#": ## if found the '#' in the string, add trees variables to 1
                    trees += 1
                else:
                    continue
    return trees

##should improve this one make more dynamic function
def findthetreesdown2(value,trails):
    slop_right = value
    pos = -value ##this is to get make sure first position of string start with 0
    trees = 0
    i = -1   ##To make sure iteration read the index of iteration as 0
    for t in trails:
        i += 1
        if (i % 2) == 0:            ## check if the iteration in the even index of iteration
            pos = pos + slop_right  ##get the current position of the trails
            if  pos < 31: 
                if t[pos] == "#":
                    trees += 1
                else:
                    continue
            else:
                pos = pos - 31       ## get the current position of the trails
                if t[pos] == "#":    ## if found the '#' in the string, add trees variables to 1
                    trees += 1 
                else:
                    continue
        else:
            continue
           
    return trees

def main():
    ## get all the trails
    trails = readfromtxt()
    ##slope 1 = Right 1, down 1.
    slope1 = findthetreesdown1(1,trails)
    ##slope2 = Right 3, down 1.
    slope2 = findthetreesdown1(3,trails)
    ##slope3 = Right 5, down 1.
    slope3 = findthetreesdown1(5,trails)
    ##slope4 = Right 7, down 1.
    slope4 = findthetreesdown1(7,trails)
    ##slope5 = Right 1, down 2.
    slope5 = findthetreesdown2(1,trails)
    ##get final result by multiply all the slopes
    result = slope1 * slope2 * slope3 * slope4 * slope5
    ##print the answer
    print("The answer for Part1: "+str(slope2))
    print("The answer for Part2: "+str(result))
if __name__ == "__main__":
    main()