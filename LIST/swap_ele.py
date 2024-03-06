'''def swapPosition(list, pos1, pos2):
  list[pos1], list[pos2] = list[pos2], list[pos1]
  return list


list = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPosition(list, pos1 - 1, pos2 - 1))
#using inbuilt list.pop()
def swapPosition(list,pos1,pos2):
    first_ele=list.pop(pos1)
    second_ele=list.pop(pos2-1)

    list.insert(pos1,second_ele)
    list.insert(pos2,first_ele)
    return list
list=[23,65,19,90]
pos1, pos2= 1, 4
print(swapPosition(list,pos1-1,pos2-1))
    
#using tuple variable
def swapPosition(list,pos1,pos2):
    get = list[pos1], list[pos2]
    list[pos2], list[pos1]=get
    return list
list=[23,65,19,90]
pos1, pos2=1, 4
print(swapPosition(list,pos1-1,pos2-1))

#using temp variable
def swapPosition(list,pos1,pos2):
    temp=list[pos1]
    list[pos1]=list[pos2]
    list[pos2]=temp
    return list
list=[23,94,97 ,23,45]
pos1,pos2=1,5
print(swapPosition(list,pos1-1,pos2-1))'''

#using enumerate
def swapPosition(list,pos1,pos2):
    for i, x in enumerate(list):
        if i==pos1:
            elem1=x
        if i==pos2:
            elem2=x
    list[pos1]=elem2
    list[pos2]=elem1
    return list
list=[23,65,19,90]
pos1 ,pos2=1, 3
print(swapPosition(list,pos1-1,pos2-1))

        
