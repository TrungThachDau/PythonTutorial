def hello(data):
    data+=1
    if data<5:
        hello(data)
    print(data)

def sum(data):
    if data==0:
        return 0
    else:
        return data+sum(data-1)

print(sum(5))
