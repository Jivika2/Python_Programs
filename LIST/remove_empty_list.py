'''list=[5,3,23,[],56,32]
print(list)
res=[i for i in list if i!=[]]
print(res)'''

lst1=[23,34,[],6,[],87,[],9,[]]
res=list(filter(None,lst1)) or list(filter(lambda x: x!=[],lst1))
print(res)
      
def empty_list_remove(list1):
    lst=[]
    for i in list1:
        if i:
            lst.append(i)
    return lst
list1=[23,34,[],33 ,[], 3,[],45,[]]
print(empty_list_remove(list1))

list1=[23,34,[],33 ,[], 3,[],45,[]]
while [] in list1:
    list1.remove([])
print(list1)
