def ppp(s):
    return s == s[::-1]


with open('121.txt','r') as f:
    s = f.read()
ans = ppp(s)

if ans:
    print("Yes")
else:
    print("No")