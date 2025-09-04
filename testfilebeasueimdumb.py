

for x in range(10):
    print(x*100)
    print("\033[2J\033[H", end="")
print("yippee")