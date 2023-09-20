#!/usr/bin/env python

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

for i in range(0, 2000001):

    for count in 0,1,2:
        if count==0:
            ht=int(i/1000000)%1000
        if count==1:
            ht=int(i/1000)%1000
        if count==2:
            ht=i%1000
            if i==0:
                print(ones[i], end=" ")

        tensdata=ht%100
        hundredsdata=int(ht/100)

        if hundredsdata>0:
            print(ones[hundredsdata], "hundred", end=" ")
        if tensdata>0 and tensdata<10:
            print(ones[tensdata], end=" ")
        if tensdata>=10 and tensdata<20:
            temp=tensdata%10
            print(teens[temp], end=" ")
        if tensdata>=20 and tensdata<100:
            temp=int(tensdata/10)%10
            temp2=tensdata%10
            if temp2>0:
                print(tens[temp], ones[temp2], end=" ")
            else:
                print(tens[temp], end=" ")
        if count==1 and ht>0:
            print("thousand", end=" ")
        if count==0 and ht>0:
            print("million", end=" ")
    print("")

