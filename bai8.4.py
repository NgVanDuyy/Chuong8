import math
print("Tính diện tích tam giác:")
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a :
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác:",S)
else:
    print("Không hợp lệ")

