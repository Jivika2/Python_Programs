#swap function using temp
def swapList(newList):
    n=len(newList)
    temp=newList[0]
    newList[0]=newList[n-1]
    newList[n-1]=temp
    return newList
newList=[12,35,9,56,24]
print(swapList(newList))

#without Using temp
def swapList(newList):
    newList[0], newList[-1]=newList[-1], newList[0]
    return newList
newList=[12,35,9,56,24]
print(swapList(newList))


#Using *operator
list=[1,2,3,4]
a, *b, c=list
print(a)
print(b)
print(c)

# Swap function
def swapList(list):
     
    start, *middle, end = list
    list = [end, *middle, start]
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))

# Swap function
def swapList(list):
     
    first = list.pop(0)   
    last = list.pop(-1)
     
    list.insert(0, last)  
    list.append(first)   
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))



def swap_first_last_3(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst
 
# Initializing the input
inp=[12, 35, 9, 56, 24]
 
# Printing the original input
print("The original input is:",inp)
 
result=swap_first_last_3(inp)
 
# Printing the result
print("The output after swap first and last is:",result)
