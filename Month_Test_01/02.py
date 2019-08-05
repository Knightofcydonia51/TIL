# 파일명 및 함수명을 변경하지 마시오.
def alphabet_count(word):
    """
    아래에 코드를 작성하시오.
    word는 소문자로만 구성되어 있습니다.
    알파벳을 key로, 갯수를 value로 가지는 딕셔너리를 반환합니다.
    """
    dict={}
    for i in word:
        dict[i]=0
    for i in word:
        dict[i]+=1
    return dict

    # dict={}
    # for char in word:
    #     if dict.get(char):
    #         dict[char]+=1
    #     else:
    #         dict[char]=1
    # return dict

    # return {char : word.count(char) for char in word}



# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
