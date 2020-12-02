import os 
from random import sample


def readfromtxt():
    files = open('input.txt', 'r') 
    all_num = [int(x.strip()) for x in files.readlines()]
    # print(all_num)
    
    return all_num

##Part1
def findtwonum(all_num):
    # print(all_num)
    arr = []
    
    samp = sample(all_num,2)
        
    get_arr = True
    while get_arr:
        two_numbers = sample(all_num,2)
        ans = sum(two_numbers)
        if ans == 2020:
            get_arr = False
            arr.extend(two_numbers)
        else:
            continue
    
    final_num = arr[0]*arr[1]
    return final_num

##part2
def findthreenum(all_num):
    arr = []
    
    samp = sample(all_num,2)
        
    get_arr = True
    while get_arr:
        three_numbers = sample(all_num,3)
        ans = sum(three_numbers)
        if ans == 2020:
            get_arr = False
            arr.extend(three_numbers)
        else:
            continue
    
    final_num = arr[0]*arr[1]*arr[2]
    return final_num

    
def main():
    all_num = readfromtxt()
    ##Part1
    ans_part1 = findtwonum(all_num)
    print("The answer for part 1: "+ str(ans_part1))
    ##Part2
    ans_part2 = findthreenum(all_num)
    print("The answer for part 2:"+str(ans_part2))
    
if __name__ == "__main__":
    main()