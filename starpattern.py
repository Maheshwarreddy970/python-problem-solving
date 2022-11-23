'''
*
**
***
****'''
space=" "
star="*"
num=4
for i in range(1,5):
    print(star*i)
print()

'''
   *
  ***
 *****
*******'''
for i in range(1,5):
    st=(i+i-1)*star
    sp=(num-i)*space
    print(sp+st)
print()
'''
   *
  **
 ***
****'''
for i in range(1,5):
  sp=(num-i)*space
  st=star*i
  print(sp+st)
print()
star="*"
space=" "
num=4
'''
****
***
**
*
'''
for i in range(0,4):
  st=star*(num-i)
  print(st)
print()
'''
*******
 *****
  ***
   *
'''
for i in range(0,4):
  sp=(i)*space
  s=7-(i+i)
  st=star*s
  print(sp+st)
print()