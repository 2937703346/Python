num = 0x02015

# 获取百位数
if num // 100 == 0:
    hundred = '0'
else:
    hundred = str(num // 100)

# 获取十位数
if num // 10 % 10 == 0:
    ten = '0'
else:
    ten = str(num // 10 % 10)

# 获取个位数
if num % 10 == 0:
    unit = '0'
else:
    unit = str(num % 10)

# 输出结果
print("数字", num, "的百位数是：", hundred)
print("数字", num, "的十位数是：", ten)
print("数字", num, "的个位数是：", unit)
