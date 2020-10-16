def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    

if __name__ == "__main__":
    l = list(map(int,input().split(' ')))
    reverseList(l,0,len(l)-1)
    print("reversed array:",l)    