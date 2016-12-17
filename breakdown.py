def change(money):
    for i in [1000,500,100,50,20,10,1]:
        denom= money/i
        if denom>0:
           print i,"*",denom,"=",i*denom
           money=money-(i*denom)           
change(1574)      
