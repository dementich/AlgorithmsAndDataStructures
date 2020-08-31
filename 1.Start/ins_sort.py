#!/usr/local/bin/python3

def ins_sort(a):
    for j in list(range(1, len(a))):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a

def main():
    a = [5, 2, 4, 6, 1, 3]
    b = ins_sort(a)
    print(b)

if __name__ == "__main__":
    main()

