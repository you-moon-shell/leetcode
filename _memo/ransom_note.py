from collections import Counter

str1 = 'abcxyz'
str2 = 'aaaaabbbbcccdd'

cnter1, cnter2 = Counter(str1), Counter(str2)

print(cnter1, cnter2)
# 積集合(共通部分を取得)
print(cnter1 & cnter2)
# 和集合(値は大きい方を優先)
print(cnter1 | cnter2)

dict1 = {'a': 1, 'b': 1, 'c': 1, 'x': 1, 'y': 1, 'z': 1}
dict2 = {'a': 5, 'b': 4, 'c': 3, 'd': 2}
# dictでは積集合を取得できない(エラーとなる)
# print(dict1 & dict2)
print(dict1 | dict2)
