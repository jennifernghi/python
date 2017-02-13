import random
import sys
import os

print ("Hello World")
print("-------------------------------------")
name = "Nghi" # string
print(name)
print("-------------------------------------")
## operator: + - * / % **(exponent 10**20 = 10^20) // floor division

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)
print("-------------------------------------")
## comparision: == != > < >= <=
## bitwise: & | ^ ~(flipping bit - > signed number) << >>
a = 60
print("60:", bin(a)) # print binary #

b = 13
print("13:", bin(b)) # print binary #

print("a & b", a&b, bin(a&b))
print("a | b", a|b, bin(a|b))
print("a ^ b", a ^ b, bin(a^b))
print("~a", ~a, bin(~a))
print("a << 2", a<<2, bin(a<<2))
print("a >> 2", a>>2, bin(a>>2))
print("-------------------------------------")
##logical and or not
##membershift: in   not in

c =10
d = 20
list = [1, 2, 3, 4, 5];

if c in list:
    print("c is available in list")
else:
    print("c not in list")

if d not in list:
    print("d is not available in list")
else:
    print("d is in list")

c = 2 # change the value
if c in list:
    print("c is available in list")
else:
    print("c not in list")
print("-------------------------------------")
##identity operators:  is (point to the same object)   is not

a = 20
b = 20
if a is b:
    print("a and b has same id")
else:
    print("a and b not have same id")

if id(a) == id(b):
    print("a and b has same id")
else:
    print("a and b not have same id")

b =30
if a is b:
    print("a and b has same id")
else:
    print("a and b not have same id")

if a is not b:
    print("a and b don't have same id")
else:
    print("a and b have same id")

print("-------------------------------------")
# while loop

count =0
while count <10:
    print("count: ", count)
    count +=1;
else: # call when while is false
    print("count now:", count,  ". stop")

print("-------------------------------------")
# foor loop
print("get letter in python string:")
for letter in "Python":
    print("current letter: ", letter)
print("-------------------------------------")
print("get element in a list:")
fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print("current fruit: ", fruit)

print("-------------------------------------")
print("get element in a list using index, range(), len():")
for index in range(len(fruits)):
    print("Current fruit: ", fruits[index])

print("-------------------------------------")
print("find prime # from 10 to 20")
for num in range(10,20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print("%d equals %d * %d" % (num, i, j))
            break
    else:
        print(num, "is a prime number")