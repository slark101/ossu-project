"""
Solution for problem set 0
https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps0/

integer conversion for log result because sample result is an integer.
"""
import math

print('Enter number x:',end=' ')
x = int(input())
print('Enter number y:',end=' ')
y = int(input())
print('x**y =',x**y)
print('log(x)',int(math.log(x,2)))
