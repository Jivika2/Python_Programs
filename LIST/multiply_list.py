#list using traversal
def multiplyList(list):
    result=1
    for x in list:
        result*=x
    return result
list=[13,4,2,3]
list1=[1,2,3,4]
print(multiplyList(list))
print(multiplyList(list1))


 #using numpy.prod()
'''import numpy
list1 = [1, 2, 3]
list2 = [3, 2, 4]
 
# using numpy.prod() to get the multiplications
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print(result1)
print(result2)'''


#using lanbda function
from functools import reduce
list=[1,3,4,5]
list1=[2,4,5,6,7,8]
result=reduce((lambda x,y:x+y), list)
result1=reduce((lambda x,y:x*y), list1)
print(result)
print(result1)

#using prod function of math library
import math
list=[12,3,4,6]
list1=[4.5,6,7,8]
res=math.prod(list)
res1=math.prod(list1)
print(res)
print(res1)

#using mul() function operator module
from operator import*
list=[2.4,6,7,8]
list1=[34,5,7]
m=1
for i in list:
    m=mul(i,m)
print(m)

#using traversal by index
def multiplyList(list):
    result=1
    for i in range(0,len(list)):
        result*=list[i]
    return result
list=[2.4,5,3,3.2,5,6]
print(multiplyList(list))

'''#using itertools.accumulate
from itertools import accumulate
list=[2,4,5,6,7]
list1=[3.1,4,6,8]
result=list(accumulate(list, (lambda x,y:x*y)))
result1=list(accumulate(list1, (lambda x,y:x*y)))
print(result[-1])
print(result1[-1])'''

#using recursive function
def product_recursive(list):
    if not list:
        return 1
    return list[0]*product_recursive(list[1:])
list=[2,4,5,6]
product=product_recursive(list)
print(product)

#using reduce() and mul() function
from functools import reduce
from operator import*
list=[2,3,4,5]
result=reduce(mul,list)
print(result)

