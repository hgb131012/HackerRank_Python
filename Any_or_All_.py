if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(any(str(num)[::-1] == str(num) for num in nums) and all(num >= 0 for num in nums))
