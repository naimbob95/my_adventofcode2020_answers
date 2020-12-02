import os 
from random import sample


def readfromtxt():
    files = open('input.txt', 'r') 
    answer = []
    for line in files:
        tmp = []
        raw_rules, pass_val = line.strip().split(':')
        min_val,max_val_char = raw_rules.strip().split('-')
        max_val,char_val = max_val_char.strip().split()

        tmp.append(int(min_val))
        tmp.append(int(max_val))
        tmp.append(char_val)
        tmp.append(pass_val)
        answer.append(tmp)
        
        
    files.close()    
    return answer

## part 1
def passwordpolicypart1(raw_pass):
    
    allow_pass = []
    for r in raw_pass:
        min_value = r[0]
        max_value = r[1]
        char_policy = r[2]
        pass_str = r[3]
        char_in_pass = pass_str.count(char_policy)
        if char_in_pass >= min_value and char_in_pass <= max_value:
            allow_pass.append(pass_str)
        else:
            continue        
    
    total_allow = len(allow_pass)
    return total_allow


## part 2
def passwordpolicypart2(raw_pass):
    
    allow_pass = []
    for r in raw_pass:
        min_value = r[0]
        max_value = r[1]
        char_policy = r[2]
        pass_str = r[3][1:]
        tmp = []

        if pass_str[min_value - 1] == char_policy:
            if pass_str[max_value - 1] == char_policy:
                continue
            else:
                allow_pass.append(pass_str)
        else:
            if pass_str[max_value - 1] == char_policy:
                allow_pass.append(pass_str)
            else:
                continue    
                
            continue
    
    total_allow_pass = len(allow_pass) 
    return total_allow_pass
    
def main():
    raw_pass = readfromtxt()
    # print(raw_pass)
    total_allow = passwordpolicypart1(raw_pass)
    print("Answer for part1: "+str(total_allow))
    total_allow2 = passwordpolicypart2(raw_pass)
    print("Answer for part2: "+str(total_allow2))
    
if __name__ == "__main__":
    main()