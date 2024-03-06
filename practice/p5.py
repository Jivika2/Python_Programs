'''Given a positive integer x, the task is to print the numbers
from 1 to x in the order as 12, 22, 32, 42, 52, ...
(in increasing order).'''
def printIncreasingPower(x):
    i=1

    while(i<x+1):
        print ( i*10+2, end = " ")
        i+=1
    #print()
x = int(input("Enter a positive integer: "))
print("The numbers in the specified pattern are:")
print( printIncreasingPower(x))       
        
