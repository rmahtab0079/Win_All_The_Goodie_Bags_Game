#same algorithm as the cpp file

def fun(l, r, stepEven, step, n):
    if(n == 1):
        print(l, r, stepEven, step, n)
        return l
    print(l,r , stepEven, step, n)
    if(n % 2 == 0):
        return fun(l, r - 2**stepEven+1, stepEven+1, step+1, n//2)
    else:
        return fun(l + 2**step, r, stepEven, step+1, (n-1)//2)

# range can be changed to whatever n (where n represents the number of participants
#In this case I am taking the case scenarios from 4120682-4120683 to find the solution to the problem I was presented

for i in range(4120682, 4120683):
    win = fun(1, i, 1, 1, i)
    print(i, " = ", win)
    print("\n\n")
