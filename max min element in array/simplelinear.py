def max_min(l):
    max = 0
    min = 999999999

    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i
    return (max, min)


if __name__ == "__main__":
    print(max_min([1, 2, 3, 4, 5]))
