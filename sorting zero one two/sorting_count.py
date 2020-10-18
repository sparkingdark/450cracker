def sorting_zot(arr):
    zero = arr.count(0)
    one = arr.count(1)
    two = arr.count(2)

    arr = arr.clear()

    arr = [[0]*zero,[1]*one,[2]*two]
    return arr

if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int,input().split(' ')))
        print(sorting_zot(arr))
        t-=1

