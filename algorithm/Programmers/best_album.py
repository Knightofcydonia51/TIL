
gen=["classic", "pop", "classic", "classic", "pop"]
pla=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    music=[]
    for i in range(len(genres)):
        music.append((genres[i],pla[i]))
    music.sort(key=lambda music:music[0])
    print(music)
    answer = []
    return answer

solution(gen,pla)