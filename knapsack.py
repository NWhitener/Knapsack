#imports needed for the assignment 

import numpy as np
import pandas 

def knapsackFiller(filePath):
   
    file = open(filePath, 'r')
    weight = file.readline().split()[1]
    print("The weight of the knapsack is: ", weight)
    numItems = file.readline().split()[1]
    print("The number of items in the file is: ", numItems)
    knapsack = np.zeros((int(numItems), 2))
    print(knapsack)
    #this is a test loop    
    for i in range(0,int( numItems)): 
        line = file.readline()
        knapsack[i][0] = int(line.split()[1])
        knapsack[i][1] = int(line.split()[3])
    print(knapsack)












def main():
    knapsackFiller('small.txt')

if __name__ == '__main__': 
    main()
