import argparse 
# def greet(name,lang):
#     greet={
#         'English': 'Hello',
#         'Spanich': 'Hola',
#         'German': 'Hallo'
#     }
#     m=f'{greet[lang]} {name}'
#     print(m)

# p=argparse.ArgumentParser('SELECT LANGUAGE REY')

# p.add_argument('name')
# p.add_argument('lang',choices=['English','Spanich','German'])

# a=p.parse_args()
# greet(a.name,a.lang)

# greet={
#         'English': 'Hello',
#         'Spanich': 'Hola',
#         'German': 'Hallo'
#     }
# p.add_argument('lang',choices=[greet.keys()])
# a=p.parse_args()
# print(a.lang)

p1=argparse.ArgumentParser()

l=p1.add_argument_group('Login DAta')
l.add_argument('--username',default="UNKNOWN")
l.add_argument('id')
l.add_argument('-p','--password')

l1=p1.add_argument_group('Personal Data')
l1.add_argument('-n','--name')
l1.add_argument('-a','--age',default=21)

a=p1.parse_args()

print(a.name)

# g=p1.add_mutually_exclusive_group(required=True)

# g.add_argument('-u','--uploading',action='store_true')
# g.add_argument('-d','--downloading',action='store_true')

# a=p1.parse_args()

# if a.uploading:
#     print('Uploading..')
# elif a.downloading:
#     print('Downloading..')
# else:
#     print('ONLY ONE IS ACCEPTED')