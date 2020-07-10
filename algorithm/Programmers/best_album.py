#
# gen=["classic", "pop", "classic", "classic", "pop"]
# pla=[700, 600, 700, 700, 2500]
#
# def solution(genres, plays):
#
#     music=[]
#     for i in range(len(genres)):
#         music.append((genres[i],pla[i],i))
#
#     answer = []
#
#     gen = list(set(genres))
#     gennum = len(gen)
#     maxi = 0
#
#     for i in range(gennum):
#         one=[]
#         hap=0
#         for k in range(len(music)):
#             if gen[i]==music[k][0]:
#                 one.append((music[k][1],music[k][2]))
#
#         print(set(sorted(one)))
#         print(sorted(one,reverse=True)[:2])
#         music.sort(key=lambda music: music[0])
#
#
#     return answer
#
#
# solution(gen,pla)
#
#
#


def solution(genres, plays):
    answer = []
    # { 장르 : 총 재생 횟수 } 사전
    playsDict = {}
    # { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
    d = {}

    # 사전들 초기화
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = playsDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [(play, i)]

    # print(playsDict,d['pop'])

    # 재생 횟수 내림차순으로 장르별로 정렬
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)

    # print(genreSort)
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬
    # 장르별로 최대 2개 선택
    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        print(d[genre])
        answer += [idx for (play, idx) in d[genre][:2]]

    return answer


if __name__ == '__main__':
   genres = ["classic", "pop", "classic", "classic", "pop"]
   plays = [700, 600, 700, 700, 2500]
   result = solution(genres, plays)
   print(result)