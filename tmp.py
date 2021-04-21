num = 2021
for i in range(1, 1000000):
    for j in str(i) :
        if j=="1":
            num -= 1
    if num == 0:
        print(i)
        break
