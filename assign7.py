#!/usr/bin/env python3

import sys
import os
import re

#Dictonaries 
int2Roman = { 
            1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'IX',
            50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
#Inverted dictonary, ex: 'M':1000, etc.
roman2Int = dict(map(reversed, int2Roman.items()))

def main():
    convertToRoman(812)     #returns "DCCCXII"
    convertToRoman(49)      #returns "XLIX"
    convertToRoman(5000)    #throws "Error - Too Large"
    convertFromRoman('CCCXIV')  #returns 314
    convertFromRoman('MCMXCIX') #returns 1999
    convertFromRoman('CXXXXI')   #returns "Error" ~ Reason illegal consectuive roman numerals
    convertFromRoman(" I  ")     #returns "Error" ~ Reason whitespace
    convertFromRoman('MMMM')    #returns "Error" ~ Reason number > 3999
    convertFromRoman('GGGY')   #returns "Error" ~ Reason not valid roman numeral character

def convertToRoman(givenInt):
    errorCheck = errorCheckInt(givenInt)
    if (errorCheck): return

    romanConversion = ''
    #Greedy Algo, take largest from roman and subtract the int value from given int.
    while givenInt > 0:
        highestInt = max([i for i in int2Roman.keys() if i <= givenInt])
        romanConversion += int2Roman[highestInt]
        givenInt -= highestInt

    print(romanConversion)

def convertFromRoman(givenRoman):
    if (checkLegalChars(givenRoman) or checkConsecutiveRoman(givenRoman)): return print("Error")

    intConversion = 0
    for i, number in enumerate(givenRoman):
        #len(givenRoman)-1 != i prevents the string index going out of range. 
        #roman2Int[givenRoman[i+1]]... sorts it accordingly so the lower number is subtracted from higher. 
        if (i != len(givenRoman)-1) and (roman2Int[givenRoman[i+1]] > roman2Int[number]):
            intConversion -= roman2Int[number]
        else:
            intConversion += roman2Int[number]          

    if (intConversion > 3999 or intConversion <= 0 or isinstance(intConversion, int) == False): return print("Error") 

    print(intConversion)

def errorCheckInt(givenInt):
    if (givenInt > 3999):
        print("Error - Too Large")
        return True
    elif (givenInt <= 0):
        print("Error - Too Small")
        return True
    elif (isinstance(givenInt, int) == False):
        print("Error - Not a Number")
        return True

def checkLegalChars(givenRoman):
    if (isinstance(givenRoman, str) == False) or re.match(r'[ \t]', givenRoman): return True

    for letters in givenRoman:
        if letters not in int2Roman.values(): return True


def checkConsecutiveRoman(givenRoman):
    count = {}
    for i in givenRoman:
        if i in count: 
            count[i] += 1
        else:
            count[i] = 1
    for i in count: 
        if count[i] >= 4: 
            return True

if __name__ == '__main__':
    main()