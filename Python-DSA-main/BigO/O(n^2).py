#loop within a loop

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#this runs n*n=n^2
print_items(10)