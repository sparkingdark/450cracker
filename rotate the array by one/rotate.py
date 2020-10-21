def rotate(arr):
    last = arr.pop()

    arr.insert(0,last)

    return arr


if __name__ == "__main__":
    t = int(input())

    while t>0:
        arr = list(map(int,input().split(' ')))

        print(rotate(arr))

        t-=1
