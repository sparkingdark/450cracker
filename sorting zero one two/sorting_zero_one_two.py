def sorting_zot(arr):
    zero = []
    one = []
    two = []

    for i in arr:
        if i==0:
            zero.append(0)
        elif i==1:
            one.append(1)
        elif i==2:
            two.append(2)
    return zero+one+two

if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int,input().split(' ')))
        print(sorting_zot(arr))
        t-=1

