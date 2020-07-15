def div(a,b =2):
    return a/b

# a = 4 로 위치인자가 들어감
print('div(4) =',div(4)) 

# a = 200 b = 5 위치인자로 넣은 결과
print('div(200, 5) =',div(200,5))

# 위치인자와 키워드인자 혼용

print('div(200, b=5) =',div(200,b=5))
print('div(a=200, b=5) =',div(a=200,b=5))
print('div(b=5, a=200) =',div(b=5,a=200))


#TypeError: div() got an unexpected keyword argument 'bc' ->키워드 인자오류
#print('div(bc=5, ac=200) =',div(bc=5,ac=200))

#SyntaxError: positional argument follows keyword argument ->위치 인자오류
#print('div(b=5, 200) =',div(b=5,200))