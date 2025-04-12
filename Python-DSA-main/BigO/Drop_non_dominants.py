def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

#this runs n*n+n or o(n^2+n) so drop the non-dominat so it becomes O(n2)
print_items(10)