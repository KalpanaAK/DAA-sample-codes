import time

def function1(txt, pat, m, n):
    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

txt = input("Enter text : ")
pat = input("Enter pattern : ")

stime = time.time()

result = function1(txt, pat, len(txt), len(pat))

etime = time.time()

print("Pattern found at index :", result)
print("Execution Time :", etime - stime)