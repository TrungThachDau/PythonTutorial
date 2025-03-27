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
def findMedian(arr):
    arr.sort()
    print(arr)
    if len(arr)%2==0:
        mid1 = arr[:1]
        mid2 = arr[:-1]
        median = (mid1 + mid2) / 2
    else:
        median = arr[len(arr)//2]
    print("Median:", median)
a= [0,1,2,4,6,5,3]
findMedian(a)