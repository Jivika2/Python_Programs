def Nmaxelement(list,N):
    final_list=[]
    for i in range(0,N):
        max1=0
        for j in range(len(list)):
            if list[j]>max1:
                max1=list[j]
        list.remove(max1)
        final_list.append(max1)
    print(final_list)
list=[13,35,23,67,432,66]
print(Nmaxelement(list,3))

#l
l=[100,192,98,456,827,87]
n=4
l.sort()
print(l[-n:])

#using traversal
arr=[]
while n:
    arr.append(l[-n])
    n-=1
print(arr)
