#Nhập dữ liệu
Năm = int(input("Nhập năm:"))
#Kiểm tra năm nhuận
if (Năm % 400 == 0) or ((Năm % 4 == 0) and (Năm % 100 !=0)) :
    print("Năm nhuận")
else:
    print("Năm không nhuận")
