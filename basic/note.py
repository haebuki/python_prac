mul=1
result=False
for _ in range(5):
    x = int(input())
    mul = mul*x
    for i in range(100):
        if mul==i**2:
            result=True
            break

if result !=True:
    print("not found")
else:
    print("found")
