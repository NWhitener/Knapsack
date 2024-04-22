#imports needed for the assignment 

import numpy 
import pandas 

def knapsackIE(filePath): 
    file = open(filePath, 'r')
    weight = file.readline().split()[1]
    print("The weight of the knapsack is: ", weight)
    numItems = file.readline().split()[1]
    print("The number of items in the file is: ", numItems)
    #this is a test loop    













def main():
    knapsackIE('small.txt')

if __name__ == '__main__': 
    main()
