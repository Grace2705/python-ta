import sys
import os


def palindrome(s):
    text = list(s)
    text = reversed(text)
    string = ""
    string = string.join(text)
    return (string == s)
    


def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
