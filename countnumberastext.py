#!/usr/bin/env python

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
bignumbers = {"decillion": 33, "nonillion": 30, "octillion": 27, "septillion": 24, "sextillion": 21, "quintillion": 18, "quadrillion": 15, "trillion": 12, "billion": 9, "million": 6, "thousand": 3, "hundreds": 0}

def numbertotext(i):
    returnstring=""
    if i<0:
        returnstring="negative "
        i*=-1
    if i==0:
        return "zero"
    for counter in bignumbers:
        multiplier=bignumbers[counter]
        ht=int(i/(1*10**multiplier))%1000

    

        tensdata=ht%100
        hundredsdata=int(ht/100)

        if hundredsdata>0:
            returnstring=returnstring+ones[hundredsdata]+ " hundred "
        if tensdata>0 and tensdata<10:
            returnstring=returnstring+ ones[tensdata] + " "
        if tensdata>=10 and tensdata<20:
            temp=tensdata%10
            returnstring=returnstring+ teens[temp] + " "
        if tensdata>=20 and tensdata<100:
            temp=int(tensdata/10)%10
            temp2=tensdata%10
            if temp2>0:
                returnstring=returnstring + tens[temp] + " " + ones[temp2] + " "
            else:
                returnstring=returnstring + tens[temp] + " "
        if ht>0 and not counter=="hundreds":
            returnstring=returnstring + counter + " "
    return returnstring.strip()

for i in range(-50, 200000001):
    print(numbertotext(i))
