def print_ex1(a,b,c):
    x1 = -b+(((b**2-4*a*c)**0.5)/(2*a))
    x2 = -b-(((b**2-4*a*c)**0.5)/(2*a))
    print(x1, "또는", x2,"이다")

print_ex1(1,-1,-2)