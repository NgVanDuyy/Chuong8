x=int(input("Nhập vào số x:"))
dem=0
if x>0 :
    for i in range (2,x):
        if x%i == 0:
            dem=1
            print(x,"không phải là số nguyên tố")
            break 
    if dem == 0:
        print(x,"là số nguyên tố")
else:
    print("Không phải số nguyên tố")
        
