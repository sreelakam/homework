def breakdown(value):
    m=()
    d=[1000,500,100,50,20,10,1]
    for amount in d:
        num=int(value/amount)
        m+=(amount,)*num
        value-=(amount*num)
        print("{} * {} = {} {}".format(amount,num,num*amount,m))
