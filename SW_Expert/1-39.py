l = sorted([4, 2, 6, 8, 10])
def finder(n):
    if n in l:
        return True
    else:
        return False

print(l)
print('5 => {}'.format(finder(5)))
print('10 => {}'.format(finder(10)))