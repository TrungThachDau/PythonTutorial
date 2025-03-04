def add(*kwargs):
    print(kwargs)
def add2(**kwargs):
    #print(kwargs)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

def add3(*args):
    print(args)
    for arg in args:
        print(arg)
def func4():
    triples = [y*3 for y in range(1,11)]
    print(triples)

list_name={
    'User':[{
        'name': 'Huy',
        'age':20
    }]
}
list_name2={
    'User':[{
        'name': 'Huy',
        'age':20
    }]
}
add2(**list_name)
# add2(a=1,b=2,c=3,d=4,e=5,f=6)
# add3(1,2,3,4,5,6)
#func4()


#Phân biệt Arg và Kwarg
#Arg: là một tuple chứa các tham số truyền vào hàm
#Kwarg: là một dictionary chứa các tham số truyền vào hàm