# Program to implement filter function 

def filter(a):
 return [x for x in a]


def even(p):
 return p%2==0
l=[1,2,3,4]
print 'Original list',l
print filter(even,range(10))
