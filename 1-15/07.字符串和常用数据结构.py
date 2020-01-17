
# 1 字符串表示的方法
str1 = 'hello,world!'
str2 = "hello,world!"
str3 = """
hello,
world!
"""
# 2 带专一类型的字符串
str4 = 'hello,\n world!'
str5 = 'hello,\t world!'
str6 = "hello,\r world!"


s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
#print(s1, s2, end='')

# s1 = 'hello ' * 3
# print(s1) # hello hello hello
# s2 = 'world'
# s1 += s2
# print(s1) # hello hello hello world
# print('ll' in s1) # True
# print('good' in s1) # False
# str2 = 'abc123456'
# # 从字符串中取出指定位置的字符(下标运算)
# print(str2[2]) # c
# # 字符串切片(从指定的开始索引到指定的结束索引)
# print(str2[2:5]) # c12
# print(str2[2:]) # c123456
# print(str2[2::2]) # c246
# print(str2[::2]) # ac246
# print(str2[::-1]) # 654321cba
# print(str2[-3:-1]) # 45


name = 'xingzhe007'
age = 29
# 输出字符串的三种方式：
print(f"Hello, {name}. you are {age}")
print("sfdsf,{name}".format(name="ffff"))
print("sdfds %s" %(name))

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))
