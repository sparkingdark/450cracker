# My Daily Trackerof 450 problems

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
- **Code**:[]()

- **Recursive way** :

```
1) Initialize start and end indexes as start = 0, end = n-1
2) Swap arr[start] with arr[end]
3) Recursively call reverse for rest of the array.

```

- **Code**:[]()



