def foo(**kwargs) :
    print('인자의 개수 : ',len(kwargs))
    print('인자는 : ',kwargs)


foo(first=10,second='a',third='b')