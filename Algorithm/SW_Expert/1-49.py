def even_maker(numlist):
    return [x for x in numlist if x%2==0]
    
print(even_maker(range(1,11)))