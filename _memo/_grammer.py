# if
if 1 == 2:
    print("if")

# for -> range(stop)
for i in range(10):
    print("for")

# for -> range(start, stop[, step])
for i in range(1, 10, 2):
    print("for")

# 偶数/奇数
if 4 % 2 == 0:
    print("偶数")

# list
_l = [1, 2]
_l.append(3)
print(_l)
_l.pop(0)
print(_l)
_l.pop(-1)
print(_l)

# loop string
_s = "string"
for c in _s:
    print(c)

# slice
_l2 = [1, 2, 3]
print(_l2[:0])
print(sum(_l2[4:]))
