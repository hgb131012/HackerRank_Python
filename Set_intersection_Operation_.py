if __name__ == '__main__':
    a, n = int(input()), set(map(int, input().split(" ")))
    b, m = int(input()), set(map(int, input().split(" ")))
    print(len(n.intersection(m)))
