import re

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""

print(text)
print('________________________________')
split_text = re.split('/s+', text)
print(split_text)


print('________________________________')
#match at least one or more space characters.
regex = re.compile('\s+')
split_text1 = regex.split(text)
print(split_text1)
