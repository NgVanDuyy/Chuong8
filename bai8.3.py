print("Nhập hệ số a,b:")
a=float(input())
b=float(input())
if a!=0 :
    x=-b/a
    print("Nghiệm phương trình bậc nhất:",x)
else:
    if b==0 :
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
