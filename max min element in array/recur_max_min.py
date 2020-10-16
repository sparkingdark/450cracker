def max_duo(a, b):
    if a > b:
        return a
    return b


def min_duo(a, b):
    if a < b:
        return a
    return b


def recur_max_min(arr, size):
    if size == 1:
        return (arr[0], arr[0])
    elif size == 2:
        return (max_duo(arr[0], arr[1]), min_duo(arr[0], arr[1]))
    else:
        pass


if __name__ == "__main__":
    pass
