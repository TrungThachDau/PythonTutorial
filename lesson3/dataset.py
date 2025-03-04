import pandas as pd



def Example1():
    myset ={
        'name': ['Trung', 'Huy', 'Tuan'],
        'age': [20, 21, 22],
        'address':['Saigon', 'Hai Phong', 'Da Nang']
    }
    a = ['Yellow', 'Green', 'Blue']

    dts = pd.DataFrame(myset)
    print(pd.options.display.max_rows)
    print(dts)
    print(dts.loc[0])
    print(dts.info())
    print('series: \n',pd.Series(a))

    print('series with label: \n',pd.Series(a, index=['a', 'b', 'c']))
