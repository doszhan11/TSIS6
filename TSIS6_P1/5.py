items = ['Mango', 'Orange', 'Apple', 'Lemon']

with open('111.txt', 'w') as f:
    for item in items:
        f.write(item + "\n")

