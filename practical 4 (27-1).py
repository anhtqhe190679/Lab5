def phan1():
    tuple1 = ('Orange', [10, 20, 30], (5, 15, 25))
    box = tuple1[1]
    print(box[1])
phan1()

def phan2():
    tuple2 = (10, 20, 30, 40)
    a = tuple2[0]
    b = tuple2[1]
    c = tuple2[2]
    d = tuple2[3]
    print(a)
    print(b)
    print(c)
    print(d)
phan2()

def phan3():
    tuple1 = (11,22)
    tuple2 = (99,88)
    tuple_box = []
    tuple_box = tuple1
    tuple1 = tuple2
    tuple2 = tuple_box
    print(f'tuple1 = ',tuple1)
    print(f'tuple2 = ',tuple2)
phan3()
    
