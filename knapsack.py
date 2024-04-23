#imports needed for the assignment 

import numpy as np
import pandas 
import time 
def knapsackFiller(filePath):
   
    file = open(filePath, 'r')
    weight = file.readline().split()[1]
    print("The weight of the knapsack is: ", weight)
    numItems = file.readline().split()[1]
    print("The number of items in the file is: ", numItems)
    knapsack = np.zeros((int(numItems), 2), dtype = int)

    
    #this is a test loop    
    for i in range(0,int( numItems)): 
        line = file.readline()
        knapsack[i][0] = int(line.split()[1])
        knapsack[i][1] = int(line.split()[3])

    return (int(weight), int(numItems), knapsack)

def knapsackIE(weight, items, sack): 
    #Base Cases: Knapsack empty  
    dpTable = np.zeros((weight+1,items+1), dtype = int)
    for j in range(0, items): 
        for w in range(0, weight+1):
            if sack[j][0] > w:
                dpTable[w][j] = dpTable[w][j-1]
            else: 
                sackValue = sack[j][0]

                dpTable[w][j] = max(dpTable[w][j-1], dpTable[(w-sackValue)][j-1]+sack[j][1])
    return dpTable[weight][items-1]             

def knapsackE(weight, items, sack): 
    dpTable = np.zeros((weight+2, 2), dtype = int)
    for j in range(0,items): 
        for w in range(0,weight+1):
            if sack[j][0] > w: 
                dpTable[w][1] = dpTable[w][0]
            else: 
                sackValue = sack[j][0]
                dpTable[w][1] = max(dpTable[w][0], dpTable[w-sackValue][0]+sack[j][1])
        dpTable[:,0] = dpTable[:,1]

        dpTable[:,1] = 0

    return dpTable[weight][0]

def knapsackBack(weight, items, sack): 
    #Base Cases: Knapsack empty  
    dpTable = np.zeros((weight+1,items+1), dtype = int)
    for j in range(0, items):
        for w in range(0, weight+1):
            if sack[j][0] > w:
                dpTable[w][j] = dpTable[w][j-1]
            else:
                sackValue = sack[j][0] 
                dpTable[w][j] = max(dpTable[w][j-1], dpTable[(w-sackValue)][j-1]+sack[j][1])
    print(dpTable)
    #Backtracking 
    itemsList = []
    weightLoc = weight
    for j in range(items-1, -1,-1):         
        if (j != 1): 
            if dpTable[weightLoc][j-1] != dpTable[weightLoc][j]: 
                print(dpTable[weightLoc][j], dpTable[weightLoc][j-1], j)
                itemsList.append(j+1)
                weightLoc = weightLoc - sack[j][0]
        else:
            if dpTable[weightLoc][j] != 0:
                itemsList.append(j)
                break
    return itemsList           







def main():
   start = time.time()
   (weight, items, knapsack)=  knapsackFiller('medium.txt')
   end = time.time()
   print("Filling took :", end - start)
   start2 = time.time()
   print(knapsackBack(weight, items, knapsack))
   end2 = time.time()
   print("Computing took: ", end2-start2)
if __name__ == '__main__': 
    main()
