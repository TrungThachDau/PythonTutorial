def func_a():
    list_a = [1,2,3,4,5] #Ordered, Changeable, Allow Duplicate
    set_b = {1,2,3,4,5} #Unordered, Unchangeable, No Duplicate
    tuple_c = (1,2,3,4,5) #Ordered, Unchangeable, Allow Duplicate
    citis = {"USA":"New York",
             "Vietnam":"Saigon",
             "Japan":"Tokyo",
             "Korea":"Seoul",
             "China":"Beijing",
            "Thailand":"Bangkok",
             }
    # print("Collection")
    # print("List: ", list_a)
    # print("Set: ", set_b)
    # print("Tuple: ", tuple_c)
    #
    # set_b.add(6)
    # print("Set after add 6: ", set_b)
    # set_b.remove(2)
    # print("Set after remove 2: ", set_b)
    #
    # print(tuple_c[1])
    #
    # print(list_a)
    # print(len(set_b))
    # # for x in list_a:
    # #     print(x,end=" ")
    # # print('\n')
    # # for x in set_b:
    # #     print(x,end=" ")
    # list_a.reverse()
    # print(list_a)
    print(dir(citis))
    print(citis.get("Vietnam"))
    citis.popitem()
    print(citis)
    for key, value in citis.items():
        print(f'{key:10} : {value}')
    print(citis.keys())
if __name__=="__main__":
    func_a()