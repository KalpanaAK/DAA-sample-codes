import time

def function(txt, pat, m, n):
    for i in range(m - n + 1):
        if txt[i:n+i] == pat:
            return i
    return -1

txt = input("Enter a text : ")
pat = input("Enter a pattern : ")

stime = time.time()

time.sleep(1)

result = function(txt, pat, len(txt), len(pat))

print("Pattern found at index :", result)

etime = time.time()

print("Execution Time :", etime - stime - 1)