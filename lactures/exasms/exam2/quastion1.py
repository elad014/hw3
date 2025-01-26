

arr = []

while True:

    x = int(input("enter pos num"))
    if x < 0:
        break
    arr.append(x)

for i in reversed(arr):
    print(i)