from random import randint
import pygal

class Tessera():
    """Класс представляющий один кубик"""
    def __init__(self, num_sides = 6):
        """По умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число от 1 до числа граней"""
        return randint(1, self.num_sides)

# tes1 = Tessera()

#Моделирование серии бросков с сохранением результатов в списке.

tes1 = Tessera()
tes2 = Tessera()
results = []
for roll_num in range(1000):
    result = tes1.roll()
    results.append(result)
#Бросок кубика
frequencies = []
for value in range(1, tes1.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)



hist = pygal.StackedBar()


hist.title = 'Results of rolling one D6 1000times.'
hist.x_labels = map(str, range(1,12))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('Others',  frequencies)
# hist.render_in_browser()
# hist.render_to_file('tessera_visual.svg')

#бросок двух кубиков с суммированием результатов
import pygal
tes1 = Tessera()
tes2 = Tessera()
#Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = tes1.roll() + tes2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = tes1.num_sides + tes2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#Визуализация результатов
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_in_browser()
# hist.render_to_file('dice_visual1.svg')
