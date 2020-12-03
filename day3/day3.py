import os 
from random import sample


def readfromtxt():
    files = open('input.txt', 'r') 
    trails = []
    for line in files:
        trails.append(line.rstrip())
        
        
    files.close()    
    return trails
    
def main():
    trails = readfromtxt()
    print(trails)
  
    
if __name__ == "__main__":
    main()