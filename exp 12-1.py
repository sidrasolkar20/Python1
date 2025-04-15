# Aim:WAP in python to transpose and find diagonal elements of a matrix.
# Name: Sidra Solkar
# UIN: 231P087   Roll No: 43
from numpy import *
# accept rows and column
r,c=[int(a) for a in input("Enter rows and column :").split()]
# accept matrix element as a string
str= input(" Enter Matrix Elements :\n")
# convert string into matrix with size r*c
x= reshape(matrix(str),(r,c))
print(" original matrix : ")
print(x)
print(" Transpose matrix : ")
y=x.transpose()
print(y)
print(" Diagonal of a matrix : ")
y=diagonal (x)
print(y)
print("Sum ofdiagonal : ")
print(sum(y))
