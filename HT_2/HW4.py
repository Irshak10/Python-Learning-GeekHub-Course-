# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

# Моя відповідь:

def fun_1(a, b, c):
	return (b*b - (4 * a * c))


def fun_2(lucky_number):
	
	if lucky_number == 8:
		h = "Ви відгадали"
	else:
		h = "Неудача"
	return h


def fun_3(title):
	return title.upper()


def fun_4():
	o = fun_1(5,6,7)
	i = fun_2(8)
	u = fun_3('it`s my unbelievable function')
	if o % 8 == 0:
		p = i + ' ' + u
	else:
		p = u
	return p


print(fun_4())