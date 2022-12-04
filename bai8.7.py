soKwh = float(input("Nhập số Kwh:"))
Tongsotien = 0
if soKwh <= 50 :
    Tongsotien = soKwh * 1.678
elif soKwh <= 100 :
    Tongsotien = 50 * 1.678 + (soKwh - 50)*1.734
elif soKwh <= 200 :
    Tongsotien = 50*1.678 + 50*1.734 + (soKwh - 100)*2.014
elif soKwh <= 300 :
    Tongsotien = 50*1.678 + 50*1.734 + 100*2.014 + (soKwh - 200)*2.2536
elif soKwh <= 400 :
    Tongsotien = 50*1.678 + 50*1.734 + 100*2.014 + 100*2.2536 + (soKwh - 300)*2.834
elif soKwh >= 401 :
    Tongsotien = 50*1.678 + 50*1.734 + 100*2.014 + 100*2.2536 + 100*2.834 + (soKwh - 400)*2.927
print("Tổng số tiền:",Tongsotien)
