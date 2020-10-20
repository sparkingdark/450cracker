def union(arr,arr2):
    has_element = set()
    if len(arr)>len(arr2):
        for i in arr:
            if i in arr2:
                has_element.add(i)
        return has_element
    else:
        for i in arr2:
            if i in arr:
                has_element.add(i)
        return has_element    

def intersection(arr,arr2):
    return set(arr).union(arr2) 


if __name__ == "__main__":
    print(union([1,2,3,4,55,56],[2,3,5,6,8,55,56]),intersection([1,2,3,4,55,56],[2,3,5,6,8,55,56]))