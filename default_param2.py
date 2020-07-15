def div(a=1 ,b=2):
    return a/b

print('div() =',div()) # 인자가 없을 경우 div(1,2)로 간주
print('div(4) =',div(4))# div(4,2)로 간주함
print('div(6, 3) =',div(6,3))

# 키워드 인자로 전달 
print('div(a=200, b=5) =',div(a=200,b=5))
print('div(b=5, a=200) =',div(b=5,a=200))