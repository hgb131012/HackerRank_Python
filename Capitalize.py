import os
import sys

def solve(s):
    result = []
    words = s.split(" ")
    for word in words:
        result.append(word.capitalize())
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
