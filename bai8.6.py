km = float(input("Nhập số km:"))
loaixe = int(input("Nhập loại xe:"))
thoigiancho = float(input("Nhập thời gian chờ:"))
giadixe = 0
tiencho = 0
tiencuoc = 0
if loaixe == 4:
    if km <= 20 :
        giadixe = 11000*0.8 + 12100*(km - 0.8)
    else:
        giadixe = 11000*0.8 + 12100*(20 - 0.8) + 10000*(km - 20)
elif loaixe == 7:
    if km <= 30 :
        giadixe = 13000*0.8 + 14100*(km - 0.8)
    else:
        giadixe = 13000*0.8 + 14100*(30 - 0.8) + 12000*(km - 30)
else:
    print("Không có loại xe bạn chọn")
if thoigiancho <= 5 :
    tiencho=0
else:
    tiencho= 800*(thoigiancho - 5)
tiencuoc = giadixe + tiencho
print("Tiền cước",tiencuoc)
