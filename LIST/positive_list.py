list1=[12,13,45,-23,56,87,-4]
for i in list1:
  if i<=0:
    print(i,end=' ')

li=[i for i in list1 if i<=0]
print(li)
# we can also print positive no's using lambda exp. 
pos_nos = list(filter(lambda x: (x <= 0), list1))
print(pos_nos)
