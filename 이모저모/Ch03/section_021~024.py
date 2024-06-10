# section_021~024.py

print('*'*50)

str1 = '내 이름은 '
str2 = '홍길동입니다.'

print(str1+str2+' 학번은 12345678 입니다.')

print('*'*50)
print()

print(str1[0])
print(str1[2])
print(str1[4])
# print(str1[7])
print()

print(str2[-1])
print(str2[-2])
print(str2[-3])
print(str2[-7])
print()

print(str1[2:4])
print(str1[:4])
print()

print(str1[-4:-2])
print(str1[:-2])
print()

print(str2[-4:])
print()

# str1[0] = "네"

# Sec 25 실습

print('*'*50)
print("Sec 25 실습시작\n")
str1 = 'Hello, my princess. Are you hungry?'
print(str1.upper())
print(str1.lower())
print(str1.title())
print()

print(str1.count('r'))
print(str1.endswith('?'))
print(str1.startswith('h'))
print(str1.lower().startswith('h'))
print()

str2 = str1.split()
print(str2)
str2 = str1.split(',')
print(str2)
str2 = str1.split('.')
print(str2)
print()

print(len(str1))
print(str1.zfill(50))
print()

