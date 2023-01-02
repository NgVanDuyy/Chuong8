#Ham Fibonacy
def fib(n):
    if n== 0 or n==1: return n 
    else:
        return fib(n-1)+fib(n-2)
x=int(input("Nhap gia tri x ="))
print("Fibonacy (", x,"),",fib(x))