# 파일명 및 함수명을 변경하지 마시오.
def can_divide(numbers, divisor):
    ans=[]
    for i in numbers:
        if i%divisor==0:
            ans.append(i)
            ans.sort()
    if ans==[]:
        ans.append(-1)
    return ans

    # answer =[number for number in numbers if not number % divisor]
    # answer = sorted(answer) if answer else [-1] 
    # return answer
        
    


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(can_divide([20, 3, 5, 7], 5))
    print(can_divide([4, 3, 2, 1], 1))
    print(can_divide([7, 11, 13], 3))
