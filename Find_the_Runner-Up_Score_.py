if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum_score = max(arr)
    print(max([score for score in arr if score != maximum_score]))
