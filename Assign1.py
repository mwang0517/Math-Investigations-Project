#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:02:18 2020

@author: Arwyn Thandrayen, Ben Thomas, Jui-Hsuan Su, Meng Wang
"""

import random
import matplotlib.pyplot as plt
#This function generates a 62-character string from the alphabet 
def getRandText():
    S=''
    alphabet = 'abcdefghijklmnopqrstuvwxyz .'
    for i in range(62):
        S += random.choice(alphabet)
    return S

#Return the score of a randomString by comparing each position to the target T
def score(randomString):
    T = "he who seeks rest finds boredom. he who seeks work finds rest."
    #If the following statement is false, the program should terminate
    assert len(randomString) == len(T)
    #If the following statement is true, we run the following program
    num = 0
    for i in range(62):
        if T[i] == randomString[i]:
            num += 1
    return num
    
# Main Program -------------------------------------------------------------
print("Welcome to the Typing Monkeys Program...")
print("====================================================================")
iterationTimes = int(input("How many times we want to generate the String? "))
scores = []
for i in range(iterationTimes):
    randomString = getRandText()
    print("The random string we generated is: " + randomString)
    rightPosiNum =score(randomString)
    scores.append(rightPosiNum)
    if (rightPosiNum == 62):
        print("We get full Mark! The random generate string is same as target string! ")
        break
    print("The score is: " + str(rightPosiNum) + " out of 62")
print("====================================================================")
print("The score we get is: ")
print(scores)
print("The maximum score is: " + str(max(scores)))
print("The minimum score is: " + str(min(scores)))
print("The average score is: " + str(sum(scores)/len(scores)))
print("====================================================================")
plt.plot(scores)
plt.title("The right position number in each iteration ")
plt.xlabel("Iteration time")
plt.ylabel("Right position numbers")
plt.show()
print("...Terminating")