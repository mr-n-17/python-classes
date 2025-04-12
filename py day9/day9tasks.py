# Command Line Arguments 

# 1.Take alist of numbers as arguments and print their average

# import sys 

# print(sys.argv)
# c=0
# m=0
# for i in sys.argv[1:]:
#     c+=int(i)
#     m+=1
# print(c/m)

# 2.Accept Filename and count how amny lines it has

# import sys 
# print(sys.argv)

# with open(sys.argv[1],'r') as f:
#     print(len(f.readlines()))

# 3.Pass two words and print the longer one

# import sys 

# print(sys.argv)

# c=0
# for i in sys.argv[1:]:
#     if len(i)>c:
#         c=len(i);d=i
# print(c,d)

# 4.check if a number is prime

# import sys 

# print(sys.argv)

# for i in sys.argv[1:]:
#     c=1
#     for j in range(2,int(i)):
#         if int(i)%j==0:
#             c=0 
#             break 
#     if c:
#         print(int(i))

# 5.accept multiple filenames and print which ones exist 

# import sys 

# print(sys.argv)

# for i in sys.argv[1:]:
#     try:
#         with open(i,'r') as f:
#             print(f.readlines())
#     except FileNotFoundError as e:
#         print(e)
    

# Argparse


# 1.add two numbers using argparse

# import argparse 

# p1=argparse.ArgumentParser()

# p1.add_argument('-n','--num1',type=int,default=0)
# p1.add_argument('-n2','--num2',type=int,default=0)

# a=p1.parse_args()

# print(a.num1+a.num2)

# 2.repeat a word 
# Goal: Accept a word and  count as arguments print the word many times

# import argparse 
# p1=argparse.ArgumentParser()

# p1.add_argument('word')
# p1.add_argument('-n','--num',default=1,type=int)

# a=p1.parse_args()

# print(a.word*a.num)


# 3.choose operation(add,subtract)
# Goal : Accept two numbers and an operation (--op add or --op sub)

# import argparse 
# p1=argparse.ArgumentParser()


# p1.add_argument('-n1','--num1',type=int,default=0)
# p1.add_argument('-n2','--num2',type=int,default=0)

# l=p1.add_mutually_exclusive_group()
# l.add_argument('-a','--add',action='store_true')
# l.add_argument('-s','--sub',action='store_true')

# a=p1.parse_args() 

# if a.add:
#     print(a.num1 + a.num2)
# elif a.sub:
#     print(a.num1 - a.num2)


# 4.multiple file inputs 
# use nargs'+' to accept a list of file names

# import argparse

# p1=argparse.ArgumentParser()

# p1.add_argument('l',nargs='+')
# a=p1.parse_args()

# print(a.l)


# 5. word counter

# import argparse

# p1=argparse.ArgumentParser()

# p1.add_argument('l',nargs='+')
# a=p1.parse_args()

# c=0
# for i in a.l:
#     c+=1
# print(c)

# print(len(a.l))

# 6.Create a User Profile
# Description:
# Collect user's name, age, and gender from command line and print profile.

# import argparse

# p1=argparse.ArgumentParser()

# p1.add_argument('username',type=str)
# p1.add_argument('-a','--age',required=True)
# p1.add_argument('-g','--gender',choices=['M',"F",'O'],required=True)

# a=p1.parse_args()

# print(a)

# 7.File Analyzer
# Description:
# Take a file name as input, and return:

# Number of lines

# Number of words

# Number of characters
# Based on flags passed.

# Arguments:

# filename (positional)

# --lines (store_true)

# --words (store_true)

# --chars (store_true)

# import argparse 

# p1=argparse.ArgumentParser()

# p1.add_argument('-f','--filename',default='data9.txt',type=str)

# p1.add_argument('-w','--words',action='store_true')
# p1.add_argument('-l','--lines',action='store_true')
# p1.add_argument('-c','--chars',action='store_true')

# a=p1.parse_args()

# with open(a.filename,'r') as f:
#     b=f.readlines()

# if a.lines:
#     print(len(b))

# if a.words:
#     c=0
#     for i in b:
#         c+=len(i.split())
#     print(c)

# if a.chars:
#     with open(a.filename,'r') as f:
#         m=0
#         for j in range(len(b)):
#             for i in f.readline(): 
#                 if i!=' ':
#                     m+=1 
#         print(m)
                
                
# 8.Temperature Converter
# Description:
# Convert temperature from Celsius to Fahrenheit or vice versa.

# Arguments:

# --value (required, float)

# --to (choices=['C', 'F'], required)
            

# import argparse 

# p1=argparse.ArgumentParser()

# p1.add_argument('-v','--value',required=True,type=float)
# p1.add_argument('-t','--to',choices=['C','F'],required=True)

# a=p1.parse_args()

# if a.to == 'F':
#     print(f'Value is in Celsius and after convert to Fahrenheit the value is {(a.value *(9/5))+32}')

# elif a.to == "C":
#     print(f'Value is in Fahrenheit and after convert to Celsius the value is {(a.value-32)*(5/9)}')



# 9.Search for Word in File
# Description:
# Search for a word in a text file and print line numbers containing that word.

import argparse 
import json

p1=argparse.ArgumentParser()

p1.add_argument('filename')
p1.add_argument('-s','--search',default='name')

a=p1.parse_args()

with open(a.filename,'r') as f:
    b=json.load(f)
    c=0
    for i in b:
        if i==a.search:
            print(c+1)
            break
        else: c+=1
    
        
        
    