
import math
from time import sleep

#currency conversion code
#take input in Rupee

dollar_conversion_multiple = 78
yen_conversion_multiple = 1.72
ukdollar_conversion_multiple = 0.011
r=1
 

def convert():
    
    global dollar_conversion_multiple
    global yen_conversion_multiple 
    global ukdollar_conversion_multiple
    global r

    toconvert = float(input("Enter the amount in Rupee you want to convert?\n"))

    convertinto = input("Enter the currency to which you want to convert? : \t \n 1. Dollar \n 2. Yen \n 3. UK Dollar \n\n ")


    if convertinto == '1':
        r =  toconvert * dollar_conversion_multiple * r
        print(r) 

    elif convertinto == '2':
        r = toconvert * yen_conversion_multiple * r
        print(r)

    elif convertinto == '3':
        r = toconvert * ukdollar_conversion_multiple * r
        print(r)

    else:
        print("Invalid Option selected, please retry")

    return convertinto, r

convert()


