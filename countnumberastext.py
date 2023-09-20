#!/usr/bin/env python

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numbertotext(i):
    returnstring=""
    for count in -1, 0,1,2:
        if count==-1:
            ht=int(i/1000000000)%1000
        if count==0:
            ht=int(i/1000000)%1000
        if count==1:
            ht=int(i/1000)%1000
        if count==2:
            ht=i%1000
            if i==0:
                #print(ones[i], end=" ")
                returnstring=returnstring+ones[i] + " "

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
                returnstring=returnstring+ tens[temp] + " " + ones[temp2]
            else:
                returnstring=returnstring+ tens[temp] + " "
        if count==1 and ht>0:
            returnstring=returnstring + "thousand "
        if count==0 and ht>0:
            returnstring=returnstring + "million "
        if count==-1 and ht>0:
            returnstring=returnstring + "billion "
    return returnstring.strip()

for i in range(0, 200000001):
    print(numbertotext(i))
