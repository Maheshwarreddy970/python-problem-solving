while True:
    try:
        num1=int(input('enter your first number\n'))
        symbol=input('enter your symbol\n')
        num2=int(input('enter your second number\n'))
        if symbol=='+':
            print(num1+num2)
        elif symbol=="-":
            print(num1-num2)
        elif symbol=='*':
            print(num1*num2)
        elif symbol=='/':
            print(num1/num2)
        elif symbol=='%':
            print((num1/num2)*100)
        else:
            print('\ninvalid symbol')
    except ValueError:
        print("enter correct input")