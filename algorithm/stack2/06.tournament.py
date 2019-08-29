#
#
# T=int(input())
#
# for i in range(T):
#     N=int(input())


arr=[1,3,2,1]

def power(base, exponent):
    if exponent==2:

    elif exponent%2==0:
        newbase=power(base,exponent/2)
        return newbase*newbase
    elif exponent==1:
        return arr[0]
    else:
        newbase=power(base,(exponent-1)/2)
        return (newbase*newbase)*base

print(power(arr,4))