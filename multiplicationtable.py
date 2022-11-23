while True:
    num=int(input('enter number\n'))
    try:
        for i in range(1,11):
            print(f'{num} x {i} = {num*i}')
    except ValueError:
        print('correct input')