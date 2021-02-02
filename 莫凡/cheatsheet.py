import re
text="abc,Abc,ABC,密码:123-56780"
m=re.search(r'Abc',text)
#<re.Match object; span=(4, 7), match='Abc'>
print(m)
#拿出来实际的东西Abc
print(m.group())
#分组好处，记得加(\d{3})
n=re.search(r'(\d{3})-(\d{5})',text)
print(n.group(1))






