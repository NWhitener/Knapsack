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
    return (int(weight), int(numItems), knapsack)

def knapsackIE(weight, items, sack): 
    #Base Cases: Knapsack empty  
    dpTable =np.zeros((weight+1,items+1))
    for i in range(1, items): 
        for j in range(1, weight):
            if sack[i][0] > j:
                dpTable[j][i] = dpTable[j][i-1]
            else: 
                sackValue = sack[i][0] 
                print(sackValue)
                dpTable[j][i] = max(dpTable[j][i-1], dpTable[j-sackValue][i-1]+sack[i][1])
                 
    print(dpTable)    









def main():
   (weight, items, knapsack)=  knapsackFiller('small.txt')
   knapsackIE(weight, items, knapsack)
if __name__ == '__main__': 
    main()
