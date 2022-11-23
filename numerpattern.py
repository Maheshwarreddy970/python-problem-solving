star="*"
space=' '
num=4
'''
1
22
333
4444
'''
for j in range(5):
  for i in range(j+1):
    print(j+1,end='')
  print()
print()

'''
1
12
123
1234
'''
for j in range(1,5):
  for i in range(1,j+1):
    print(i,end='')
  print()
print()

'''
1
21
321
4321
'''
for j in range(0,5):
  for i in range(j+1,0,-1):
    print(i,end='')
  print()
print()

'''
4444
3333
2222
1111
'''
for j in range(4,0,-1):
  for i in range(4,0,-1):
    print(j,end='')
  print()
print()

'''
4444
333
22
1
'''
for j in range(4,0,-1):
  for i in range(j+1,1,-1):
    print(j,end='')
  print()
print()

'''
4321
321
21
1
'''
for j in range(4,0,-1):
  for i in range(j,0,-1):
    print(i,end='')
  print('')