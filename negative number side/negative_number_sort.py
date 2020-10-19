def neg_sort(arr):
    for i in arr:
        if i<0:
            store = i
            arr.remove(i)
            arr.insert(0,store)
    print(arr)


if __name__ == "__main__":
    t = int(input())

    while t>0:
        arr = list(map(int,input().split(' ')))

        neg_sort(arr)

        t-=1

