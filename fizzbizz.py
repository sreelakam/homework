def fizzbizz(n):
    for i in range(1,n+1):
        if i % 3==0 and i % 5==0:
           print("fizzbizz")
        elif i % 5==0:
             print("bizz")
        elif i % 3==0:
             print("fizz")
        else:
            print(i)
