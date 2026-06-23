if __name__ == '__main__':
    t = int(input())
    for n in range(1, t+1):
        a, b = input().split()
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
