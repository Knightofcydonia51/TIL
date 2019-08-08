def max_maker(a):
    i = 0
    maximum=a[i]
    while len(a)>i:
      if maximum<a[i]:
        maximum=a[i]
        i+=1
      else:
        i+=1
    return maximum
  a=[3,5,4,1,8,10,2]
  print('max({}) => {}'.format(", ".join(map(str,a)), max_maker(a)))