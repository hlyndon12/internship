def sum(x,n):
    add = 0.0
    for i in range(1,n+1):
        add += 1/(x**i)
    print(add)

sum(3,10)