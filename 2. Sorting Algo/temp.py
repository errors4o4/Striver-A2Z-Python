n=5

def addNature(i,sum):
  if ( i<1):
    print(sum)
    return
  addNature(i-1,sum*i)

addNature(n,1)
