if __name__ == '__main__':
    countries = set()
    n = int(input())
    for i in range(1, n + 1):
        country = input().strip()
        countries.add(country)
    print(len(countries))
