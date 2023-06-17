'''
a = True
b = True
c = False
'''

'''
n = int(input("Nhập n: "))
if (n % 2 == 0):
    print(n,"là số chẳn")
'''

'''
print("1 là quả táo")
print("2 là quả cam")
print("3 là quả xoài")
print("4 là quả khác")
qua = int(input("nhập quả cần bỏ vào giỏ: "))
if (qua == 1):
    print("bỏ vào giỏ a")
elif (qua == 2):
    print("bỏ vào giỏ b")
elif (qua == 3):
    print("bỏ vào giỏ c")
else :
    print("bỏ vào giỏ d")
'''


n = float(input("nhập n: "))
if(n > 0):
    print("trị tuyệt đối của", n, "là:", round(n))
else:
    print("trị tuyệt đối của", n, "là:", round( n * (-1)))