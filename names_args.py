def greet(*names) :		# names는 가변인자이다
	print(names)
    for name in names :
	    print('안녕하세요', name, '씨')

greet('홍길동','양만춘','이순신') # 인자가 3개
greet('James','Thomas') # 인자가 2개