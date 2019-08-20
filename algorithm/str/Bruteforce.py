def bruteForce(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt=0
        for j in range(len(pattern)):
            if text[i+j]!=pattern[j]:
                break
            else:cnt+=1
        if (cnt>=len(pattern)) : return i
    return -1


text="TTTTAACCA"
pattern = "TTA"
patternLength=len(pattern)
textLength=len(text)

print(bruteForce(text, pattern))