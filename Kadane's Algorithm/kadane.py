def kadane_algorithm(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in arr:
        max_ending_here = max_ending_here+i

        if max_so_far<max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

 
if __name__ == "__main__":
    print(kadane_algorithm([1,2,33,4,5,5,-1,-2]))   