def print_ex1(a,b,c):
    x1 = -b+(((b**2-4*a*c)**0.5)/(2*a))
    x2 = -b-(((b**2-4*a*c)**0.5)/(2*a))
    #print(x1, "또는", x2,"이다")
    return x1,x2

# 한번에 전체를 반환받는 법
root = print_ex1(1,5,6)
print(root)

# 각각을 따로 따로 반환받는 법
root1,root2 = print_ex1(1,5,6)
print('r1 값은',root1)
print('r2 값은',root2)


#SyntaxError: positional argument follows keyword argument
#root3 = print_ex1(1,b=5,6)
#print(root3)


root3 = print_ex1(1,c=6,b=5)
print(root3)