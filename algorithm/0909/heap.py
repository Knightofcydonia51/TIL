import heapq

heap=[7,2,5,3,4,6]
heapq.heapify(heap)
print(heap)
while heap:
    print(heapq.heappop(heap), end= " ")

heap=[3,1,4,16,23,12]
heapq.heapify(heap)
print(heap)
while heap:
    print(heapq.heappop(heap), end= " ")