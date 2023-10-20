
N, M = map(int, input().split())
pattern = ".|."
for i in range(1, (N // 2) + 1):
    line = (pattern * (2 * i - 1)).center(M, "-")
    print(line)
welcome_line = "WELCOME".center(M, "-")
print(welcome_line)
for i in range((N // 2), 0, -1):
    line = (pattern * (2 * i - 1)).center(M, "-")
    print(line)