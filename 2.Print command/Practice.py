### 1
print('ข้อ1')
print('Hello')
print("Hello")
print('-----------')

### 2
print('ข้อ2')
print('Hello World')
print("Hello World")
print('-----------')

## 3
print('ข้อ3')
print('hello_python')
print("hello_python")
print('-----------')

## 4
print("Merry X'Mas")
print('Merry X\'Mas')

## 5
print('I want to ask you "why dont\'you drive to work?"')

## 6
print('"I don\'t have a car"')

## 7
print('ํYou got a new job !? That\'s So exciting')

## 8
print('สวัสดีวันจันทร์')
## 9
print('ความแตกต่างระหว่างคนเก่งและคนไม่เก่ง คือ "การใช้เวลาว่าง\nให้เป็นประโยชน์"')
## 10
print('/\\/\\/\\')
## 11

print('a\nan\nant')
## 12
print('\t*\n*\t*\t*\n\t*')

## 13
print('*\t+\t*\n+\t*\t+\n*\t+\t*')
## 14 
print('Just because something\n thinks differently fromyou,\ndoes that means it\'t not thiking ?')
print('')
print('''Just because something 
 thinks differently fromyou 
 does that means it\'t not thiking ?
 ''')
## 15
print('\\\t\t/\n\tx\n/\t\t\\')
## 16
print(25)
## 17
print('%f'%100)
## 18
import math
print('%.15f'%math.pi)
## 19
a =2
print(a)
## 20
a = 12.5
print(a)

## 21
a = 2
b = 3
print('%d x %d = %d'%(a,b,a*b))

## 22
a = 2
b = 3

print('%d + %d = %d + %d = %d'%(a,b,b,a,a+b))
print('2 + 3 = 3 + 2 = {}'.format(a+b))
print('{} + {} = {} + {} = {}'.format(a,b,b,a,a+b))

## 23

a = 2
b = 3
c = 5

print('%d*(%d + %d) = %d*%d +%d*%d'%(a,b,c,a,b,b,c))
print(f'{a}*({b} + {c}) = {a}*{b} + {b}*{c}')

##24
a = 2.4
b = 2.5

print('%.1f + %.1f  = %.4f'%(a,b,a+b))

## 25
a = 5
b = 2
c = float(a)
d = float(b)
#print(type(c))

print('%.2f - %.2f = %.4f'%(c,d,c-d))

## 26

birthday = 25
print('ฉันเกิดวันที่ %d ธันวาคม'%birthday)
print('ฉันเกิดวันที่ {} ธันวาคม'.format(birthday))
print(f'ฉันเกิดวันที่ {birthday} ธันวาคม')

## 27 
a = 5
b = 100

print('%d เท่าของ %d มีค่าเท่ากับ %d'%(a,b,a*b))

## 28
a = 3.5
print('เขามีเงินเยอะกว่าฉัน %.2f บาท'%a)

## 29

a = 5

print('ฉันได้กำไร %d %%'%a)

## 30 

a = 2
b = 3.5

print('เมื่อวานฉันขาดทุน %d %% วันนี้ฉันได้กำไร %.2f %%'%(a,b))