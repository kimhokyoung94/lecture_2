def print_name():
    print("홍길동")
    print("양만춘")
    print("이순신")
    print("안중근")

def print_name2(name):
    for i in range(len(name)):
        print(i+1,'번째는',name[i])
name_date = ['홍길동', '양만춘', '이순신', '안중근','김호경']


print_name2(name_date)