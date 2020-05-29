def fact(n):
    if n == 0:
        data=1
    else:
        data=n * fact(n-1)
    return data 

n=int(input("a number"))
result=fact(n)
print(result)