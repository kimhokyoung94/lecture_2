    def arg_kwarg_param(*args,**kwargs) :
   
    print(len(args))
    print(len(kwargs))
    print(args,kwargs)
    return args , kwargs
    

#arg_kwarg_param(10,20,first=10,second='a',third='b')
result1,result2 = arg_kwarg_param(10,20,first=10,second='a',third='b')
print(result1)
print(result2)



###def arg_kwarg_param_1(**kwargs,*args) :
   
#    print(len(args))
#    print(len(kwargs))
#    print(args,kwargs)
#    return args , kwargs
    

#arg_kwarg_param(10,20,first=10,second='a',third='b')
#result3,result4 = arg_kwarg_param_1(first=10,second='a',third='b',10,20)
#print(result3)
#print(result4)
