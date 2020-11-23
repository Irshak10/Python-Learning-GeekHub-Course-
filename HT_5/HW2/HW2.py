#2. Програма-світлофор.
#   Створити програму-емулятор світлофора для авто і пішоходів.
#   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#   Приблизний результат роботи наступний:
#      Red        Green
#      Red        Green
#      Red        Green
#      Red        Green
#      Yellow     Green
#      Yellow     Green
#      Green      Red
#      Green      Red
#      Green      Red
#      Green      Red
#      Yellow     Red
#      Yellow     Red
#      Red        Green
#      .......

# Моя відповідь: 

import time

def traffic_light(n):
   
   a = iter(n)
   while True:
      try:
         yield next(a)
         time.sleep(3)
                  
      except StopIteration:
         a = iter(n)


for elem in traffic_light(['Green', 'Yellow_G', 'Red', 'Yellow_R']):
   i = 0
   while i < 4:
      if elem == 'Green':
         print(f'Для транспорту зараз: {elem}    | а для пішоходів зараз: Red')
         i += 1
         time.sleep(3)
      elif elem == 'Yellow_G':
         print(f'Для транспорту зараз: {elem} | а для пішоходів зараз: Red')
         i += 2
         time.sleep(1)
      elif elem == 'Red':
         print(f'Для транспорту зараз: {elem}      | а для пішоходів зараз: Green')
         i += 1
         time.sleep(3)
      elif elem == 'Yellow_R':
         print(f'Для транспорту зараз: {elem} | а для пішоходів зараз: Green')
         i += 2
         time.sleep(1)
      