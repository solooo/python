n = input("请输入一个数N：")
sum = 0
print(list(range(int(n))))
for i in range(int(n)):
    sum += i + 1
print("1到N的和为：", sum)
