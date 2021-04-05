z = eval("("+input("enter in this format x,y,a,b\n")+")")
x,y,a,b = z[0],z[1],z[2],z[3]

ans = ( ((x+(1/y))**a) * ((x-(1/y))**b)) / ( ((y+(1/x))**a) * ((y-(1/x))**b) )

print(ans)