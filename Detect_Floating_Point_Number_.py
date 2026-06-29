if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n = input()
        if "." not in n:
            print(False)
        else:
            try:
                n = float(n)
                print(True)
            except ValueError:
                print(False)
