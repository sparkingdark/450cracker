def Kth_max_min(l,n,k):
    l.sort()
    return (l[k-1],l[-k])


if __name__ == "__main__":
     t = int(input())

     while t>0:
        n = int(input())
        arr = list(map(int,input().split(' ')))
        k = int(input())

        print(Kth_max_min(arr,n,k))

        t-=1

