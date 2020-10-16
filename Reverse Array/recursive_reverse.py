def recur_rev_arr(l,start,end):
    if start >= end:
       return
    l[start],l[end] = l[end],l[start]
    recur_rev_arr(l,start+1,end-1)


if __name__ == "__main__":
    l = list(map(int,input().split(' ')))
    recur_rev_arr(l,0,len(l)-1)
    print("reversed array:",l)   