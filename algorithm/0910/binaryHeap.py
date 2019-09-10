import heapq
import sys
sys.stdin=open('binaryHeap.txt')

def finder(anc):
    ans=0
    while 1:
        ans+=anc
        anc=heap[((heap.index(anc)+1)//2)-1]
        if heap.index(anc)==0:
            ans += anc
            break
    return ans

T=int(input())
for i in range(T):
    N=int(input())
    heap=[int(x) for x in input().split()]
    heapq.heapify(heap)
    anc = heap[((heap.index(heap[-1])+1)//2)-1]
    if N>3:
        print('#{} {}'.format(i + 1,finder(anc)))
    else:
        print('#{} {}'.format(i+1,anc))

