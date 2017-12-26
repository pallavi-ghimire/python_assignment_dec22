num = int(input("Enter a number: "))
di = dict()
for i in range(1, num + 1):
    di.update({i : i**2})

print(di)
