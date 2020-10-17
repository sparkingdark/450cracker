import heapq

def find_kth_largest(arr,k):
    heap_store = []
    for i in arr:
        heapq.heappush(heap_store,i)
    print(heap_store)    
    for i in range(k):
        heapq.heappop(heap_store)
    print(heap_store)

    return heap_store[-1]


if __name__ == "__main__":
    t = int(input())

    while t>0:
        n = int(input())

        arr = list(map(int,input().split(' ')))
        k = int(input())
        print(find_kth_largest(arr,k))

        t-=1