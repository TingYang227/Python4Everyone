
import re


handle = open('regex_sum_test.txt')
mysum = 0

mylist = list()
cnt = 0
for line in handle:
    line = re.findall('[0-9]+', line)
    if line != []:
        line = [int(x) for x in line]
        print(line)
        cnt = cnt + len(line)
        mysum = mysum + sum(line)


print('My Sum:', mysum)
print('The total number to be added is:', cnt)


"""
import re

hand = open("regex_sum_test.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
"""
