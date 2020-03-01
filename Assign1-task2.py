#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:32:51 2020

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
randomString = getRandText()
for i in range(iterationTimes):
    offSpring = randomString
    
    # The following code random generate the string and calculate its score
    print("The random string we generated is: " + randomString)
    print()
    rightPosiNum =score(randomString)
    print("The score we get for original string is: " + str(rightPosiNum))
    print()
    
    # We can end the loop if the random generate string is the same as target string
    if (rightPosiNum == 62):
        print("We get full Mark! The random generate string is same as target string! ")
        break
    
    # The following code update each character of randomString 
    # with a probability of 1/62
    for j in range(62):
        num = random.randint(1,62)
        if(num ==1):
            offSpring = offSpring[0:j] + random.choice('abcdefghijklmnopqrstuvwxyz .') + offSpring[j+1:]
    
    # The following code display the offSpring and calculate its score                    
    print("The offSpring we generated is: " + offSpring)
    print()
    rightPosiNumOff =score(offSpring)
    print("The score we get for offSpring is: " + str(rightPosiNumOff))
    print()
    
    #The following code replace the randomString if the score of offSpring is higher
    if(rightPosiNumOff > rightPosiNum):
        randomString = offSpring
        
print("====================================================================")
print("The string we finally generated is: " + randomString)
print("The score we get is: " + str(score(randomString)))
print("====================================================================")
print("...Terminating")