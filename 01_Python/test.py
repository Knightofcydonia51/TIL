# def positive_num(numbers):
#     plus=[]
#     for i in numbers:
#         if i>=0:
#             if i%1==0:
#                 plus.append(i)
#     return sum(plus)

# print(positive_num([0.77,3,0.22,3.33]))
# print(positive_num([-1,-3,-4]))




# def calc(equation):
#     l=[]
#     cnt=-1
#     memory=0
#     for num in equation:
#         cnt+=1
#         if num=='+':
#             if memory==0:
#                 if cnt==0:
#                     pass
#                 else:
#                     l.append(equation[memory:cnt])
#                     memory=cnt+1
#             else:
#                 l.append(equation[memory-1:cnt]) #4-8
#                 memory=cnt+1
#         elif num=='-':
#             if memory==0:
#                 if cnt==0:
#                     pass
#                 else:
#                     l.append(equation[memory:cnt])
#                     memory=cnt+1
#             else:
#                 l.append(equation[memory-1:cnt]) #4-8
#                 memory=cnt+1
#         elif cnt==len(equation)-1:
#             if equation[memory-1]=='-':
#                 l.append(equation[memory-1:len(equation)])
#             else:
#                 l.append(equation[memory:len(equation)])
#     return sum(list(map(int,l)))

# print(calc('123+2-124'))
# print(calc('-12+12-7979+9191'))
# print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

# class Point:
#
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#
#     def __str__(self):
#         return 'Point:({},{})'.format(self.x, self.y)
#
# class Circle():
#
#     def __init__(self, center, r):
#         self.center=center
#         self.r=r
#
#     def get_area(self):
#         return 3.14*(self.r)**2
#
#     def get_perimeter(self):
#         return 2*3.14*self.r
#
#     def get_center(self):
#         return '({},{})'.format(self.center.x,self.center.y)
#
#     def __str__(self):
#         return 'Circle:({},{}),r:{}'.format(self.center.x,self.center.y,self.r)
#
#
#
# p1=Point(3,5)
# print(p1)
# c1=Circle(p1,3)
# print(c1.get_area())
# print(c1.get_perimeter())
# print(c1.get_center())
# print(c1)
#
# p2 = Point(4, 5)
# c2 = Circle(p2, 1)
# print(c2.get_area())
# print(c2.get_perimeter())
# print(c2.get_center())
# print(c2)
#
# def calc(equation):
#     """
#     아래에 코드를 작성하시오.
#     equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
#     계산된 결과를 정수로 반환합니다.
#     """
#     eq_re=equation.replace('+', ' +').replace('-', ' -')
#     eq_sp=eq_re.split()
#     eq_list = list(map(int,eq_sp))
#     result =  sum(eq_list)
#     return result

T=int(input())
def electric_bus():
    for i in range(T):
        charge = 0
        num=list(map(int,input().split(' ')))
        K=num[0];N=num[1];M=num[2]
        station=list(map(int,input().split(' ')))
        pointer=0
        fuel=K
        charge_point=(-1)
        while pointer<N:
            charge_point += 1
            last_point=station[charge_point]
            if last_point==station[-1]:
                last_point=N
            if fuel<0:
                break
            while pointer<last_point:
                fuel-=1
                pointer+=1
                if fuel<0:
                    charge=0
                    break
                if pointer==station[charge_point]:
                    if pointer==station[-1]:
                        if fuel>=N-station[-1]:
                            pass
                        else:
                            charge+=1
                            fuel=K
                    elif fuel>=station[charge_point+1]-station[charge_point]:
                        pass
                    else:
                        charge+=1
                        fuel=K
        print(charge)
electric_bus()
