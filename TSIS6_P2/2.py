def test(a):
    dd = 0
    cc = 0
    d = {"UPPER_CASE": dd, "LOWER_CASE": cc}

    for c in a:
        if c.isupper():
            dd += 1
        elif c.islower():
            cc += 1
        else:
            pass

    d["UPPER_CASE"] = dd
    d["LOWER_CASE"] = cc

    return d

with open('121.txt', 'r') as f:
    a = f.read()

r = test(a)
print(r)
