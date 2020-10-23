<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css" />
</head>



<a class="github-fork-ribbon" href="https://github.com/sparkingdark/450cracker" data-ribbon="Fork me on GitHub" title="Fork me on GitHub">Fork me on GitHub</a>



# My Daily Trackerof 450 problems :hello:

450 competitive programming questions daily update.So let's start.

## problems on array

### Number 1 :smiley: reverse the array.

- used language: python
- Approach:Iterative,Recursive

#### Description:

```
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

```

- **Iterative way** :

```
1) Initialize start and end indexes as start = 0, end = n-1
2) In a loop, swap arr[start] with arr[end] and change start and end as follows :
start = start +1, end = end – 1

```

- **Code**:[iterative solution](https://github.com/sparkingdark/450cracker/blob/main/Reverse%20Array/reverse_iterate.py)

- **Recursive way** :

```
1) Initialize start and end indexes as start = 0, end = n-1
2) Swap arr[start] with arr[end]
3) Recursively call reverse for rest of the array.

```

- **Code**:[recursive solution](https://github.com/sparkingdark/450cracker/blob/main/Reverse%20Array/recursive_reverse.py)

### Number 2 find max and min in a array.

- used language: python
- Approach:Iterative

#### Description:

find the maximum and minimum element in a array.

```
Input  : arr[] = {1, 2, 3}
Output : Max = 3,Min = 1

Input :  arr[] = {4, 5, 1, 2}
Output : Max = 5,Min = 1

```

- **Using simple Linear search**:

```
Initialize values of min and max as minimum and maximum of the first two elements respectively.
Starting from 3rd, compare each element with max and min, and change max and min accordingly (i.e., if the element is smaller than min then change min, else if the element is greater than max then
change max, else ignore the element)

```

- **Code**:[simple linear search approach to find max and min element](https://github.com/sparkingdark/450cracker/blob/main/max%20min%20element%20in%20array/simplelinear.py)

- **Using Recursive Approach**:

Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

```
Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return the pair of max and min

```

- **code**:[recursive way](https://github.com/sparkingdark/450cracker/blob/main/max%20min%20element%20in%20array/recur_max_min.py)


### Problem 3 Find the "Kth" max and min element of an array 

- used language: python
- Approach: Iterative Sorting

#### Description:

Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

```
Input:
2               #testcase
6               #arraysize n
7 10 4 3 20 15  #array
3               #nth smallest and biggest
5
7 10 4 20 15
4

Output:
7
15

```
- **Approach**:Iterative sorting

```
1.First sort the element
2.Access the elements by index
3.Return Kth min and max element from the array using index

```


- **Code**:[Kth max and min in O(nlogn) time](https://github.com/sparkingdark/450cracker/blob/main/kth%20max%20and%20min%20element/sorting_kth.py)

- **Approach**:Using Max Heap

```
1.Construct a max heap of size n
2.insert all the elements into it
3.Pop k-1 element from it
4.Kth largest element is the reside the root of the max heap

```


- **Code**:[Kth max and min in O(n+klogn) time](https://github.com/sparkingdark/450cracker/blob/main/kth%20max%20and%20min%20element/usingmaxheap.py)


### Problem 4 Sort an array of 0s, 1s and 2s.

- used language: python
- Approach:simple Iterative Approach

#### Description:
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

```
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

```

- **simple Iterative approach using 3 array**:

```
1. First loop through array
2.create 3 array 0,1,2
3.if element = 0 push to zero array
4.repeat for 1 and 2
5.return concatinated list.

```

- **Code**:[simple iterative approach](# My Daily Trackerof 450 problems :hello:

450 competitive programming questions daily update.So let's start.

## problems on array

### Number 1 :smiley: reverse the array.

- used language: python
- Approach:Iterative,Recursive

#### Description:

```
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

```

- **Iterative way** :

```
1) Initialize start and end indexes as start = 0, end = n-1
2) In a loop, swap arr[start] with arr[end] and change start and end as follows :
start = start +1, end = end – 1

```

- **Code**:[iterative solution](https://github.com/sparkingdark/450cracker/blob/main/Reverse%20Array/reverse_iterate.py)

- **Recursive way** :

```
1) Initialize start and end indexes as start = 0, end = n-1
2) Swap arr[start] with arr[end]
3) Recursively call reverse for rest of the array.

```

- **Code**:[recursive solution](https://github.com/sparkingdark/450cracker/blob/main/Reverse%20Array/recursive_reverse.py)

### Number 2 find max and min in a array.

- used language: python
- Approach:Iterative

#### Description:

find the maximum and minimum element in a array.

```
Input  : arr[] = {1, 2, 3}
Output : Max = 3,Min = 1

Input :  arr[] = {4, 5, 1, 2}
Output : Max = 5,Min = 1

```

- **Using simple Linear search**:

```
Initialize values of min and max as minimum and maximum of the first two elements respectively.
Starting from 3rd, compare each element with max and min, and change max and min accordingly (i.e., if the element is smaller than min then change min, else if the element is greater than max then
change max, else ignore the element)

```

- **Code**:[simple linear search approach to find max and min element](https://github.com/sparkingdark/450cracker/blob/main/max%20min%20element%20in%20array/simplelinear.py)

- **Using Recursive Approach**:

Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

```
Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return the pair of max and min

```

- **code**:[recursive way](https://github.com/sparkingdark/450cracker/blob/main/max%20min%20element%20in%20array/recur_max_min.py)


### Problem 3 Find the "Kth" max and min element of an array 

- used language: python
- Approach: Iterative Sorting

#### Description:

Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

```
Input:
2               #testcase
6               #arraysize n
7 10 4 3 20 15  #array
3               #nth smallest and biggest
5
7 10 4 20 15
4

Output:
7
15

```
- **Approach**:Iterative sorting

```
1.First sort the element
2.Access the elements by index
3.Return Kth min and max element from the array using index

```


- **Code**:[Kth max and min in O(nlogn) time](https://github.com/sparkingdark/450cracker/blob/main/kth%20max%20and%20min%20element/sorting_kth.py)

- **Approach**:Using Max Heap

```
1.Construct a max heap of size n
2.insert all the elements into it
3.Pop k-1 element from it
4.Kth largest element is the reside the root of the max heap

```


- **Code**:[Kth max and min in O(n+klogn) time](https://github.com/sparkingdark/450cracker/blob/main/kth%20max%20and%20min%20element/usingmaxheap.py)


### Problem 4 Sort an array of 0s, 1s and 2s.

- used language: python
- Approach:simple Iterative Approach

#### Description:
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

```
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

```

- **simple Iterative approach using 3 array**:

```
1. First loop through array
2.create 3 array 0,1,2
3.if element = 0 push to zero array
4.repeat for 1 and 2
5.return concatinated list.

```

- **Code**:[simple iterative approach](https://github.com/sparkingdark/450cracker/blob/main/sorting%20zero%20one%20two/sorting_zero_one_two.py)


- **alternate approach using count method**:

```
1.count the 0,1 and 2 number in array
2.return a array with the counted number of 0,1,and 2

```

- **code**:[count method 0 1 2 sorting](https://github.com/sparkingdark/450cracker/blob/main/sorting%20zero%20one%20two/sorting_count.py)


- **Dutch National Flag Algorithm OR 3-way Partitioning:**:

- a[1..Lo-1] zeroes (red)
- a[Lo..Mid-1] ones (white)
- a[Mid..Hi] unknown
- a[Hi+1..N] twos (blue)


```
At first, the full array is unknown. There are three indices – low, mid and high. Initially, the value of low = mid = 1 and high = N.

If the ith element is 0 then swap the element to the low range, thus shrinking the unknown range.
Similarly, if the element is 1 then keep it as it is but shrink the unknown range.
If the element is 2 then swap it with an element in high range.
Algorithm:
Keep three indices low = 1, mid = 1 and high = N and there are four ranges, 1 to low (the range containing 0), low to mid (the range containing 1), mid to high (the range containing unknown elements) and high to N (the range containing 2).
Traverse the array from start to end and mid is less than high. (Loop counter is i)
If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1
If the element is 1 then update mid = mid + 1
If the element is 2 then swap the element with the element at index high and update high = high – 1 and update i = i – 1. As the swapped element is not processed
Print the output array.

```

- **code**:[3 way partioning to solve 0 1 2 ](https://github.com/sparkingdark/450cracker/blob/main/sorting%20zero%20one%20two/dutch_national_flag.py)




### Problem 5 Move all negative numbers to beginning and positive to end with constant extra space.

- used language: python
- Approach:Quicksort partitioning process.

#### Description:
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
Examples : 

```
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6

Output: -12 -13 -5 -7 -3 -6 11 6 5

```
Note: Order of elements is not important here.


- **approach**:
The idea is to simply apply the partition process of quicksort. pop the element negative store element
after that insert at 0th position of the array.

- **Code**:[quicksort partitioning approach to solve](https://github.com/sparkingdark/450cracker/blob/main/negative%20number%20side/negative_number_sort.py)

### Problem 6 find the union and Intersection of two sorted array.

- used language: python
- Approach:using set property,Iterative approach

#### Description:
Given two sorted arrays, find their union and intersection.

```
Input : arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6} 
Output : Union : {1, 2, 3, 4, 5, 6, 7} 
         Intersection : {3, 5}

Input : arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10} 
Output : Union : {2, 4, 5, 6, 8, 10} 
         Intersection : {6}

```

- **Approach used**:simple iterative one

```
1.first find the maximum length of the array 
2.then iterate through the maximum array
3.if element in arr
4.then push to set
5.return the set

```

- **Code**:[simple iterative approach](https://github.com/sparkingdark/450cracker/blob/main/finding%20union%20and%20intersection%20of%20two%20sorted%20array/union_intersection.py)


### Problem 7 Cyclically rotate an array by one .

- used language: python
- Approach:

#### Description:

Given an array, cyclically rotate an array by one.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then following line contains 'n' integers forming the array. 

Output:
Output the cyclically rotated array by one.

```
Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

```

- **approach**:

```
1) Store last element in a variable say x.
2) Shift all elements one position ahead.
3) Replace first element of array with x.

```


- **Code**:[rotate](https://github.com/sparkingdark/450cracker/blob/main/rotate%20the%20array%20by%20one/rotate.py)

### Problem 8 Kadane's Algorithm.

- used language: python
- Approach:Simple iterative approach

#### Description:

Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.


- **approach**:Simple Iterative approach

```
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far
```


- **Code**:[simple iterative approach](https://github.com/sparkingdark/450cracker/blob/main/Kadane's%20Algorithm/kadane.py)
