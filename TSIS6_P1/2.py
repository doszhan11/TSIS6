import os

with open(r"111.txt", "r") as f:
    aa = f.read()

if os.path.exists(aa):
    print("Путь существует")

    if os.access(aa, os.R_OK):
        print("Доступ на чтение есть")
    else:
        print("Нет доступа на чтение")

    if os.access(aa, os.W_OK):
        print("Доступ на запись есть")
    else:
        print("Нет доступа на запись")

    if os.access(aa, os.X_OK):
        print("Доступ на выполнение есть")
    else:
        print("Нет доступа на выполнение")
else:
    print("Путь не существует")
