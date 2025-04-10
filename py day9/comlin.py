# import sys 

# print('hello')
# print(sys.argv)

# print(sys.argv[0])
# c=0
# for i in sys.argv[1:]:
#     c+=int(i)
# print(c)

# import argparse

# p=argparse.ArgumentParser()

# p.add_argument('name',help='ENTER YOUR NAME')
# p.add_argument('colors',nargs='+')
# p.add_argument('color',choices=['red','green'])
# # p.add_argument('id',nargs='*',default=101)
# # p.add_argument('--age',nargs='?',default=21)
# # p.add_argument('--gender',help='MALE/FEMALE')
# # p.add_argument('zipcode',type=int)
# # p.add_argument('-e','--email',required=True)
# # p.add_argument('-t','--true',action='store_false')

# a=p.parse_args()

# print(a.name,a.colors,a.color)

import argparse

p=argparse.ArgumentParser()
#     description='Enter the name from command prompt'
# )

# p.add_argument('-n','--name',metavar='Name',required=True)

# args=p.parse_args()

# m=f'Hello {args.name}'
# print(m)
p.add_argument('name')
p.add_argument('-s','--somevalue',action='store_const',const=9)

a=p.parse_args()
print(a.name,a.somevalue)