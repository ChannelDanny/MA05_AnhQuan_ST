'''
n = int(input("Nhập n: "))
if (n % 2 == 0):
    print(n,"là số chẳn")
else:
    print(n,"là số lẻ")
'''


x = int(input("nhập điểm: "))
if (x < 5) :
    print("Học sinh yếu")
elif (x >= 5) :
    print("Học sinh trung bình")
elif (x >= 7) :
    print("Học sinh khá")
elif (x >= 9) :
    print("Học sinh giỏi")


'''
nam = int(input('Nhập năm: '))
if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print('Nam nhuan')
else:
    print('Nam khong nhuan')
'''

'''
Thang = int(input("nhập tháng: "))
if Thang in (1,3,5,7,8,10,12):
    print("Tháng", Thang ,"có 31 ngày")
elif Thang in (4,6,9,11):
    print("Tháng", Thang ,"có 30 ngày")
elif Thang==2:
    nam = int(input('Nhập năm: '))
    if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
        print("Tháng", Thang ,"có 29 ngày")
    else:
        print("Tháng", Thang ,"có 28 ngày")
'''

'''
Thang = int(input("nhập tháng: "))
if Thang < 13:
    if Thang in (1,2,3):
        print("Tháng", Thang, "Nằm trong quý 1")
    elif Thang in (4,5,6):
        print("Tháng", Thang, "Nằm trong quý 2")
    elif Thang in (7,8,9):
        print("Tháng", Thang, "Nằm trong quý 3")
    elif Thang in (10,11,12):
        print("Tháng", Thang, "Nằm trong quý 4")
else:
    print("Lỗi")
    '''