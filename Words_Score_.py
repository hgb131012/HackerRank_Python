if __name__ == '__main__':
    count = 0
    n = int(input())
    words = input().split()
    vowels = ["a", "e", "i", "o", "u", "y"]
    for word in words:
        v = [c for c in word if c in vowels]
        if len(v) % 2 == 0:
            count = count + 2
        else:
            count = count + 1
    print(count)
