# 如果需要写一个长字符串，跨越了2行或更多行，但是不使用三引号包含的字符串，解决办法如下两种：
t = "This is not the best way to join two long strings " + \
    "together since it relies on ugly newline escaping."

s = ("This is not the best way to join two long strings "
     "together since it relies on ugly newline escaping.")
# -------------------------------------------------------------------

# 获取字符串对应unicode编码
val = ord('A')

# unicode编码获取对应字符串
str001 = chr(ord('A'))
# -------------------------------------------------------------------

# 分片操作
seq = 'I() have a dream'
# 只是原字符串的copy，不会修改原字符串
seq001 = seq[:2] + "wanggw" + seq[2:]
# -------------------------------------------------------------------

# 字符串常用方法
# 方法s.center()
str002 = "eagageateaegiojo"
str003 = str002.center(20, '@')

# 方法s.join()
str004 = "8".join('abced')
strlist001 = ["I", "have", "a", "dream"]
str005 = " ".join(strlist001)

# 方法s.split(t, n)
strlist = str002.split('a', 1)

if '__main__' == __name__:
    print(t)
    print("--------------------------")
    print(s)
    print("--------------------------")
    print('%s对应unicode编码整数值:%s' % ('A', str(val)))
    print("--------------------------")
    print('%s编码整数值对应字符串%s' % (val, str001))
    print("--------------------------")
    # 检查原字符串是否被修改
    print('检查原字符串seq是否被修改:%s' % seq)
    # 分配组装后的seq:I(wanggw) have a dream
    print('分配组装后的seq:%s' % seq001)
    print("--------------------------")
    print("返回字符串中间子字符串:%s" % str003)
    print("--------------------------")
    print("s.join方法使用:%s" % str004)
    print("--------------------------")
    print("s.split进行对%s按%s切割:%s" % (str002, 'a', strlist))
    print("--------------------------")
    print("s.join使用字符串列表%s作为参数连接字符串:%s" % (strlist001, str005))


