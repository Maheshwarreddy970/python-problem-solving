'''creating a function to swap first and last element of list'''
def swaplist(slist):
  leng=len(slist)
  tem=slist[0]
  slist[0]=slist[leng-1]
  slist[leng-1]=tem
  return slist
