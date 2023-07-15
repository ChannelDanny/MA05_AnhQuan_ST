'''
j=[]
for i in range(10, 50):
    if (i%3==0):
       j.append(str(i))
print (','.join(j))
'''

'''
tong = 0
n = int(input("hãy nhập vào số n:"))
for i in range(0, n+1):
    tong += i
print ("Tổng là: ", tong)
'''

'''
n = int(input("nhập 1 số Nguyên:"))
sum = 0
 
for i in range(1, n):
    if n%i == 0:
        sum += i

if n == sum:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo");
'''

'''
n = int(input("Nhập vào một số tự nhiên: "))
for i in range(2, n):
    if n % i == 0:
        print("Số {0} không phải số nguyên tố".format(n))
        break
else:
    print("Số {0} là số nguyên tố".format(n))
    '''

