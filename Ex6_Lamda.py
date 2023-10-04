#Lamda 
a=[1,2,3]
b=[12,34,56]
print(list(map(lambda x: x*x, a)))
print(list(map(lambda x,y: x*y, a,b)))

#filter this function returns either true or false

fib= [0,1,1,2,3,5]
result = list(filter(lambda z: z%2 == 0, fib))
print(result)
#more lambda is used in RDD and Spark, reduce 
#reduction will take 2 elements at one time and perform the action or logic.

from functools import reduce
print(reduce(lambda x,y: x+y, [23,45,56,42]))

f = lambda a,b: a if (a>b) else b 
print(reduce(f, [47,11,12,201,34]))

print(reduce(lambda a,b: a if (a>b) else b, [47,11,212,201,34]))

#here summation will behave as a lambda fundtion only
def summation(x,y):
    return x + y 
print(reduce(summation, [23,52,3,44,12]))

