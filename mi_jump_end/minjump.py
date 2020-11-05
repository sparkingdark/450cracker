'''
first calculate length
store = first element
go to arr[store]
store = arr[store] if store<=len
jump++

'''

def min_jump(arr,n):

    jumps = [0 for i in range(n)]

    if n==0 or arr[0]==0:
        return float('inf')
    jumps[0] = 0

    for i in range(1, n): 
        jumps[i] = float('inf') 
        for j in range(i): 
            if (i <= j + arr[j]) and (jumps[j] != float('inf')): 
                jumps[i] = min(jumps[i], jumps[j] + 1) 
                break
    print(jumps)        
    return jumps[n-1] 


if __name__ == "__main__":
    print(min_jump([1,3,5,8,9,2,6,7,6,8,9],11))       