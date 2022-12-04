def BMI(height,weight):
    bmi=weight/(height*height)
    return bmi
Kg=float(input("Nhập cân nặng:"))
M=float(input("Nhập chiều cao:"))
bmi=BMI(M,Kg)
print("BMI=",bmi)
if bmi<18.5:
    print("Gầy")
elif bmi <=24.99:
    print("Bình Thường")
else:
    print("Béo")
