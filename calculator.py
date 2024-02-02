#python to make a simple calculator for two numbers

print('Two Numbers Below:')
x=int(input('Enter First number:'))
y=int(input('Enter Second number:'))
ch=0
while ch<5:
    print('Calculator Menu')
    print('1.ADD')
    print('2.SUBTRACTION')
    print('3.MULTIPLY')
    print('4.DIVISION')
    print('5.EXIT')
    ch=int(input('Enter Your Choice:'))
    if ch==1:
        c=x+y
        print('Sum:',c)

    elif ch==2:
        c=x-y
        print('Difference:',c)

    elif ch==3:
        c=x*y
        print('Product:',c)

    elif ch==4:
        c=x/y
        print('Quotient:',c)

    elif ch==5:
        break
    else:
        
        print('INVALID CHOICE') 

    
    



