def ninenine():
    result=[]
    for i in range(2,10):
      l=[]
      for k in range(1,10):
        if (i*k%3==0 or i*k%7==0) and k!=9:
          continue
        elif k==9:
          result.append(l)
        else:
          l.append(i*k)
    return result
  
  print(ninenine())