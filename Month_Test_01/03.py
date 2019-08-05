def summary(word):
    # alpha=word[0]
    # weight=0
    # ans=''
    # pointer=0
    # for i in word:
    #     if i==alpha:
    #         weight+=1
    #     else:
    #         ans+=alpha
    #         ans+=str(weight)
    #         weight=1
    #     alpha=i
    #     pointer+=1
    #     if pointer == len(word):
    #         ans+=alpha
    #         ans+=str(weight)
    # return ans

    result=[]
    tmp_list=[]

    for char in word:
        if tmp_list and tmp_list[-1]!=char:
            result.append(tmp_list[-1])
            result.append(f'{len(tmp_list)}')
            tmp_list.clear()
        tmp_list.append(char)

    result.append(tmp_list[-1])
    result.append(f'{len(tmp_list)}')

    return ''.join(result)


print(summary('aabbaacc'))
print(summary('ffgggeeeef'))
print(summary('abcdefg'))