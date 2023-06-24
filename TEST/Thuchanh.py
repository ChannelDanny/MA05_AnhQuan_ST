'''
T = int(input("nhập loại tài liệu: "))
P = int(input("nhập số trang: "))
C = int(input("nhập số bản cần in: "))
if (T == 1):
    X = P * C
    print("Số lượng giấy cần dùng là", X)
elif (T == 2):
    X = P * C / 2
    print("Số lượng giấy cần dùng là", round(X))
'''

x = int(input("Số kWh người dùng tiêu thụ trong tháng là: "))
if (x < 50):
    print("Tiền điện phải trả là:", x * 1.728)
elif (x >= 51):
    print("Tiền điện cần phải trả là:", x * 1.768)
elif (x >= 101):
    print("Tiền điện cần phải trả là:", x * 2.074)
elif (x >= 201):
    print("Tiền điện cần phải trả là:", x * 2.612)
elif (x >= 301):
    print("Tiền điện cần phải trả là:", x * 2.919)
elif (x >= 401):
    print("Tiền điện cần phải trả là:", x * 3.015)