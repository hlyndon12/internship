def sum(x,n,add):
    if n>=1:
        return sum(x,n-1,add+1/(x**n))
    else:
        return add

print(sum(3,10,0))