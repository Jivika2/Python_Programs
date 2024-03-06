product=0
def arr_remainder(arr,d,n):
    product=1
    for i in range(n):
        product*=arr[i]
    return product%d
d=11
n=6
arr=[100,10,5,25,35,14]
print(arr_remainder(arr,d,n))
    
#Find remainder of arr[0]*arr[1]*...*arr[n-1]
def findremainder(arr,lens,n):
    mul=1
    for i in range(lens):
        mul=(mul*(arr[i]%n))%n
    return mul%n
arr=[100,10,5,25,35,14]
lens=len(arr)
n=11
print(findremainder(arr,lens,n))

#Using functools reduce
from functools import reduce
def remainderAfterMultiplication(arr,n):
    result=reduce(lambda x, y:(x*y) % n, arr)
    return result
arr1=[100,10,5,25,35,14]
n1=11
result1=remainderAfterMultiplication(arr1,n1)
print(result1)
arr2=[100,10]
n2=5
print(remainderAfterMultiplication(arr2,n2))

    
