#Ma sinh vien: B20DCCN497
#Ho ten: Pham Hong Phong
#Nhom: 01

import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist
congiap = ["Ty","Suu","Dan","Mao","Thin","Ty.","Ngo","Mui","Than","Dau","Tuat","Hoi"]

print("Nhap lua chon tu 1-4:")
print("1. Chuyen ngay duong lich sang am lich.")
print("2. Chuyen ngay gio duong lich sang am lich.")
print("3. Chuyen ngay am lich sang duong lich.")
print("4. Chuyen ngay gio am lich sang duong lich.")
choice = int(input())

if choice == 1:
    print("Nhap ngay duong lich:")
    print("Nhap ngay:")
    ngay = int(input())
    print("Nhap thang:")
    thang = int(input())
    print("Nhap nam:")
    nam = int(input())
    solar = Solar(nam,thang,ngay)
    lunar = Converter.Solar2Lunar(solar)
    print("Ngay am lich duoc chuyen la:",end = " ")
    print(lunar.day,lunar.month,lunar.year,sep="/")
elif choice == 2:
    print("Nhap ngay gio duong lich:")
    print("Nhap gio:")
    gio = int(input())
    print("Nhap ngay:")
    ngay = int(input())
    print("Nhap thang:")
    thang = int(input())
    print("Nhap nam:")
    nam = int(input())
    res=""
    solar = Solar(nam,thang,ngay)
    lunar = Converter.Solar2Lunar(solar)
    if gio >= 23:
        res = congiap[0]
    else:
        for i in range(1,12):
            if gio >= (i-1)*2+1 and gio < (i*2+1):
                res = congiap[i]
    print("Ngay gio am lich duoc chuyen la:",end = " ")
    print("Gio",res,end=" ngay ")
    print(lunar.day,lunar.month,lunar.year,sep="/")
elif choice == 3:
    print("Nhap ngay am lich:")
    print("Nhap ngay:")
    ngay = int(input())
    print("Nhap thang:")
    thang = int(input())
    print("Nhap nam:")
    nam = int(input())
    lunar = Lunar(nam,thang,ngay)
    solar = Converter.Lunar2Solar(lunar)
    print("Ngay am lich duoc chuyen la:",end = " ")
    print(solar.day,solar.month,solar.year,sep="/")
elif choice == 4:
    print("Nhap ngay gio am lich:")
    print("Nhap gio:")
    gio = str(input())
    print("Nhap ngay:")
    ngay = int(input())
    print("Nhap thang:")
    thang = int(input())
    print("Nhap nam:")
    nam = int(input())
    res=""
    lunar = Lunar(nam,thang,ngay)
    solar = Converter.Lunar2Solar(lunar)
    if gio == congiap[0]:
        print("Ngay gio duong lich duoc chuyen la:",end = " ")
        print("Tu 23 gio ngay hom truoc den 1 gio",end=" ngay ")
        print(solar.day,solar.month,solar.year,sep="/")
    else:
        for i in range(1,12):
            if gio == congiap[i]:
                print("Ngay gio duong lich duoc chuyen la:",end = " ")
                print("Tu",(i-1)*2+1,"gio den",(i*2+1),"gio",sep=" ",end=" ngay ")
                print(solar.day,solar.month,solar.year,sep="/")
else:
    print("Nhap khong dung, bye!")