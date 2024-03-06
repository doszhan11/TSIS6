import os

with open(r"111.txt", "r") as f:
    aa = f.read()

if os.path.exists(aa):
    print("Путь существует")

    base = os.path.basename(aa)
    dirr = os.path.dirname(aa)

    print(f"Базовое имя: {base}")
    print(f"Каталог: {dirr}")
else:
    print("Путь не существует")
