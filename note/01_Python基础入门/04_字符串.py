# 字符串用来表示一段文本信息，字符串是程序中使用的最多的数据类型
s = 'hello'
# 在Python中字符串需要使用引号引起来
# 如果不使用引号，那么他不会被解释为字符串，而是解释为一个变量去引用，这个引号可以是单引号，也可以是双引号，但是不能混合使用
s = 'hello'
s1 = "hello"
print (s)
print (s1)
# e = 'hello"
# print (e)


# 相同的引号之间不能嵌套
# s2 = "子曰："学而时习之，不亦乐乎""
s2 = '子曰：”学而时习之，不亦乐乎“'
print (s2)
print (s2)
# 长字符串 
# 单引号和双引号不能跨行使用
shi = "锄禾日当午，\
汗滴禾下土；\
谁知盘中餐，\
粒粒皆辛苦。"
print(shi)

# 使用三重引号来表示一个长字符串，三重引号可以换行，并且可以保留字符串中的格式
shi1 = '''锄禾日当午，
汗滴禾下土；
谁知盘中餐，
粒粒皆辛苦。'''
print(shi1)

# 转义字符 可以使用 \ 作为转义字符
s3 = "子曰：\"学而时\t习之，\t不亦乐乎\""
print(s3)
#    \'     表示'
#    \"    表示"
#    \t    表示制表符
#    \n   表示换行符
#    \\    表示反斜杠
#    \uxxxx   表示Unicode编码
u = '\u0040'
print (u)