# 3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

# Моя відповідь:

def season(month):
    if month in (12, 1, 2):
        print("Зима")
    elif month in (3, 4, 5):
        print("Весна")
    elif month in (6, 7, 8):
        print("Літо")
    elif month in (9, 10, 11):
        print("Осінь")
    else:
        print("Введені не вірні данні")
    return


season(12)
