 # 2.Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна принтануть і вернуть суму, яка буде на рахунку.

#Моя відповідь:


def bank(a, years, percents = 10):
	
	for n in range(years):
		a = a + (a * (percents * 0.01))
	print(f'Через {years} довгих років на рахунку матимемо {a} uah')
	return

bank(1000, 5)