# class Circle:
#     pi = 3.14
#     x = 0
#     y = 0
#     r = 0

#     def __init__(self, r, x, y):
#         self.r = r
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.pi * self.r * self.r

#     def circumference(self):
#         return 2 * self.pi * self.r

#     def center(self):
#         return (self.x, self.y)


# sol1 = Circle(3, 2, 4)

# area1 = sol1.area()
# print(f'넓이 : {area1}')

# duldul = sol1.circumference()
# print(f'둘레 : {duldul}')

numbers = [3, 1, 2]
print(numbers.sort())
print(numbers) # [1,2,3]

a=(sorted(numbers)) # 1 2 3

def greeting():
    print('hi')

a = greeting()
print(a)