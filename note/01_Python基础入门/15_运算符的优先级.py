# 运算符的优先级
# 	和数学中一样，Python中的运算符也是 先乘除，后加减
a = 1 + 2 *3
print(a)

# 与或运算的优先级
# 	
# 	如果 优先级一样高  或者 or的优先级高，则先算或后算与，则运算结果是3
# 	如果and的优先级高，则先算与后算或，则运算结果是1
a = 1 or 2 and 3
print(a)