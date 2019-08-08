def test(n):
    # ans=list(filter(lambda x:x%2==0 ,n))
    return list(map(lambda x:x**2, list(filter(lambda x:x%2==0 ,n))))
  print(test(range(1,11)))