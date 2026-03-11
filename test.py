from collections import desue

s = desue()

# إضافة عنصر
s.append(10)
s.append(20)
s.append(30)

print(s)   # desue([10, 20, 30])

# إزالة أول عنصر
x = s.popright()

print(x)   # 10
print(s)   # desue([20, 30])