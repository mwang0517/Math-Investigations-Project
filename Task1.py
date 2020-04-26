#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:29:49 2020

@author: mengwang
"""

import random

def printSquare(X):
    #Prints the contents of a Latin square to the screen in a neat way       
    for i in range(n):
        for j in range(n):
            print(X[i][j], end="\t")
        print(end="\n")
        
def rootSolution(n):
    # if number of givens is 0, then we need to generate root solution
    # each element can be generated through the formula (i+j)%n
    # i and j represent the number of rows and columns and n is the size of the matrix
    A = [[((i + j) % n) for j in range(n)] for i in range(n)]
    printSquare(A)

            
# Main Program: Ask the user to specify the input file.
filename = input("Enter problem file name >> ")

# Now read the input file line by line 
numberOfGivens = 0
n = 0
with open(filename, "r") as f:
    # Read the first line of the file to get the value for n
    line = f.readline().split()
    n = int(line[0])
    # Now define the nxn array to hold the puzzle and read the rest of the file
    puzzle = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        line = f.readline().split()
        
        #Check what we have already had in each row, and add it to the temp list
        temp= []  
        for j in range(n):
            puzzle[i][j] = int(line[j])
            if puzzle[i][j] != -1:
                numberOfGivens += 1
                temp.append(puzzle[i][j])
                
        #After checking what we have, we start to modify the matrix with value(-1)
        #Note we need to make sure we do not have duplicate value in each row.  
        for j in range(n):
            puzzle[i][j] = int(line[j])
            # when we do not read -1(It is the given number), we need to add numberOfGivens
            if puzzle[i][j] != -1:
                numberOfGivens += 1
            # when we read -1, we change it to a random number from(0,n-1)
            # note the number we generate cannot appear twice in each row.
            else:
                number = random.randint(0,n-1)
                flag = False
                while (flag == False):
                    if number not in temp:
                        puzzle[i][j] = number
                        temp.append(puzzle[i][j])
                        flag = True
                    else:
                        number = random.randint(0,n-1)
                         
print(filename, "has been read in correctly.")

# The following lines are for testing purposes and can be deleted
print("n           =", n)
print("num. givens =", numberOfGivens)

# The following lines are for checking whether we neee to generate root solution
if(numberOfGivens!=0):
    printSquare(puzzle)
else:
    print("Root Solution")
    rootSolution(n)
    
