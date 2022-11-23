ordch=int(input('inter ord number of alphabet\n'))
'''
A
BB
CCC
DDDD'''
if ordch>64 and ordch<123:
  for i in  range(0,5):
    for j in range(0,i+1):
      print(chr(ordch+i), end="")
    print()
else:
  print("enter correct char number")
print()

'''
A
AB
ABC
ABCD'''
if ordch>64 and ordch<123:
  for i in  range(0,5):
    for j in range(0,i+1):
      ordch=ordch+j
      print(chr(ordch), end="")
    print()
else:
  print("enter correct char number")
print()

'''
AAAA
AAAA
AAAA
AAAA'''
if ordch>64 and ordch<123:
  for i in  range(0,5):
    for j in range(0,4):
      print(chr(ordch), end="")
    print()
else:
  print("enter correct char number")
print()
'''
ABCD
FIJK
LMNO
PQRS'''
if ordch>64 and ordch<123:
  for i in  range(0,4):
    for j in range(0,4):
      ordch=ordch+1
      print(chr(ordch), end="")
    print()
else:
  print("enter correct char number")
print()
