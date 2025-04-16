n=input('ENTER A VALUE')
out='hello    '+n 

with open('helloit.txt','w') as f:
    f.write(out)