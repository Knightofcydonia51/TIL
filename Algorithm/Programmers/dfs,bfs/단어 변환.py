def bfs(begin,target,words):
    global answer
    result=0
    visited=[0 for i in range(len(words))]
    q=[begin]

    while q:
        w=q.pop()
        if w == target:
            return
        for i in range(len(words)):
            cnt=0
            for k in range(len(words[i])):
                if w[k]!=words[i][k]:
                    cnt+=1
                    if cnt>1:break
            if cnt==1 and visited[i]!=1:
                visited[i]=1
                q.append(words[i])
        answer+=1



def solution(begin, target, words):
    global answer
    answer = 0
    if target not in words:
        return 0
    else:
        bfs(begin,target,words)
        print(answer)
        return answer

answer=0
solution(begin="hit", target="cog", words=["hot", "dot", "dog", "lot", "log","cog"])
