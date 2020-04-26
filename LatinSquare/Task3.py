#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:03:16 2020

@author: mengwang
"""

import random
from random import choice
import matplotlib.pyplot as plt

def printSquare(X):
    #Prints the contents of a Latin square to the screen in a neat way       
    for i in range(n):
        for j in range(n):
            print(X[i][j], end="\t")
        print(end="\n")

def rootSolution(n):
    # if number of givens is 0, then we need to generate root solution
    # each element can be generated through the formula (i+j)%n
    # i and j represent the index of rows and columns and n is the size of the matrix
    A = [[((i + j) % n) for j in range(n)] for i in range(n)]
    printSquare(A)
    
def cost(Y):
    # This function calculates the cost of a matrix
    cost = 0
    for i in range(n):
        tempList = []
        # It adds numbers of the current column to the tempList
        for j in range(n):
            tempList.append(Y[j][i])
        # For the current column, it finds which value is not in the tempList.
        for ele in range(n):
            if(ele not in tempList):
                cost += 1    
    return cost

def specialPos():
    # It finds the position of the given number and save them into list
    point = []
    for i in range(int(len(specialPosition)/2)):
        ele = specialPosition[2*i:2*i+2]
        point.append([ele for i in range(1)])      
    return point


def swap(Z):
    # This function random chooses one row and two different columns
    # Defube row, col1, col2 as global variables to make sure other functions can also access them
    global row
    global col1
    global col2
    row = random.randint(0,n-1)
    col1 = random.randint(0,n-1)
    col2 = choice([i for i in range(0,n-1) if i not in [col1]])
       
    # It makes sure we do not change the number of the given position
    points = specialPos()
    while([[row,col1]] in points):
        col1 = random.randint(0,n-1)
    while([[row,col2]] in points):
        col2 = choice([i for i in range(0,n-1) if i not in [col1]])
               
    # It change the number of two columns in the same line.
    Z[row][col1], Z[row][col2] = Z[row][col2], Z[row][col1]
    return Z

def changeBack(Z,row,col1,col2):
    # This function is called after compare the new puzzle with the last-step puzzle
    # if the cost is higher in the new puzzle, we need to chenge it back to the last step
    Z[row][col1], Z[row][col2] = Z[row][col2], Z[row][col1]
    return Z
              
# Main Program: Ask the user to specify the input file.
filename = input("Enter problem file name >> ")

# Now read the input file line by line 
numberOfGivens = 0
n = 0
specialPosition = []
with open(filename, "r") as f:
    # Read the first line of the file to get the value for n
    line = f.readline().split()
    n = int(line[0])
    # Now define the nxn array to hold the puzzle and read the rest of the file
    puzzle = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        line = f.readline().split()
        
        #Check the number we already had in each row, and add it to the temp list
        temp= []  
        for j in range(n):
            puzzle[i][j] = int(line[j])
            if puzzle[i][j] != -1:
                temp.append(puzzle[i][j])
                     
        #After checking what we have, we start to modify the matrix with value(-1)
        #Note we need to make sure we do not have duplicate value in each row.  
        for j in range(n):
            puzzle[i][j] = int(line[j])
            # when we do not read -1(It is the given number), we need to add numberOfGivens
            if puzzle[i][j] != -1:
                numberOfGivens += 1
                specialPosition.append(i)
                specialPosition.append(j)
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
print("n           =", n)
print("num. givens =", numberOfGivens)
print("-------------------------------------------------------------")


# The following lines are for when the number of given numbers is not euqal to 0.
moneyList = []
if(numberOfGivens!=0):
    print("The puzzle we randomly generated is: ")
    printSquare(puzzle)
    money = cost(puzzle)
    print("The cost of randomly generated puzzle is: " + str(money))  
    print("-------------------------------------------------------------")  
    # The following lines swap the elements of the puzzle
    time = int(input("How many times you want to swap the puzzle? "))  
    for i in range(time):
        # if we generate the root solution, the loop stop in advance
        if(money ==0):
            print("We generate the root solution during the swap times!");
            break
        # The following lines change the element of the puzzle and get the cost of the new puzzle
        print("#########################################################") 
        print("The new puzzle we generate in the interation " + str(i) + " is: ")
        printSquare(swap(puzzle))
        print("The cost of the new puzzle is: " + str(cost(puzzle)))
        print("#########################################################")
        # if the cost of new puzzle is lower, update the money variable
        # if not, we need to change the new puzzle back to the last step
        if (cost(puzzle) < money):
            money = cost(puzzle)
        else:
            backOrigPuzzle = changeBack(puzzle,row,col1,col2)          
        print("The puzzle we have in the iteration " + str(i)+ " is: ")
        printSquare(puzzle)
        print("The cost is: " + str(money))   
        moneyList.append(money)
    print("-------------------------------------------------------------")
    print("The final puzzle we get is: ")
    printSquare(puzzle)
    print("The cost for the final puzzle is: " + str(money))  
    print("-------------------------------------------------------------")
    print("The cost for each iteration is: ")
    print(moneyList)
    plt.plot(moneyList)
    plt.xlabel("Iteration time")
    plt.ylabel("cost")
    plt.title("The relationship between cost and iteration")
    plt.show()
# The following lines are for when the number of given numbers is euqal to 0.
# It represents we have the root solution directly.
else:
    print("Root Solution")
    rootSolution(n)
    print("The cost for this puzzle is 0!")

