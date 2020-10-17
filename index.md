<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.3/gh-fork-ribbon.min.css" />
</head>

<body>

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


### Problem # Find the "Kth" max and min element of an array 

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
- **Approach**:

```
1.First sort the element
2.Access the elements by index
3.Return Kth min and max element from the array using index

```


- **Code**:[Kth max and min in O(nlogn) time](https://github.com/sparkingdark/450cracker/blob/main/kth%20max%20and%20min%20element/sorting_kth.py)

</body>