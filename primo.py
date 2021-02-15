print(2);print(3);print(5)
x=7
while True:
    if str(x).endswith('5'):
        pass
    else:
        for i in range(3,x+2,2):
            if i==x:
                print(x)
            elif x%i!=0:
                pass
            else:
                break
    x+=2