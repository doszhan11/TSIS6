with open('111.txt', 'r') as f, open('A.txt', 'w') as s:
    for l in f:
        s.write(l)
