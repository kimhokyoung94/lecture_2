def print_star(n=1):
    for _ in range(n):
        print('**********************')

print_star()
print("다음은 위치인자로 4를 넣었을 때 이다 \n")
print_star(4)
print("다음은 키워드인자로 4를 넣었을 때 이다 \n")
print_star(n=4)