import matplotlib.pyplot as plt

# x_dots = [i for i in range(-9,9)]
# y_dots = [i**3 for i in range(-9,9)]
# inp_values = [i for i in range(-10,11)]
# squares = [i**3 for i in range(-10,11)]
# color = (0.1, 0.5, 0.1)
# #c- задает либо цвет, либо параметр (х или у) по которому ставится цветовая карта. cmap - цветовая карта, edgecolor- цвет по значениям или по RGB(1,1,1), s - size
# plt.scatter(x_dots,y_dots, c= y_dots, cmap=plt.cm.cool, edgecolor=color,s=40)
# # plt.plot(inp_values,squares, squares, linewidth=5) # linewidth - толщина
# #назначение заголовка диаграммы и меток осей.
# plt.title("Square numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("WOW", fontsize=14)
# #Назначение размера шрифта и оформление делений на осях
# plt.tick_params(axis='y', labelsize=20) # axis=both - на обоих осях which: minor major both - какая-то ебота
# plt.show()
#bbox_inches отсекает от диаграммы лишние пропуски
# plt.savefig('cubes_plot1.png')

from random import choice

#Найти карты цветов для построения линий
class RandomWalk():
    """Класс для генерирования случайных блужданий"""
    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        x_direction = choice([1,-1])
        x_distance = choice([1,2,3,4,5,6,7,8])
        x_step = x_direction * x_distance
        #отклонение нулевых перемещений
        # if x_step == 0:
        #     return self.get_step()
        return x_step

    def fill_walk(self):
        """Вычисляет все точки блуждания"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            #Вычисление следующий значений x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



while True:
    rw = RandomWalk(100000)
    rw.fill_walk()
    print(plt.style.available)
    plt.style.use('dark_background')
    # plt.style.use(['dark_background', 'presentation'])
    #Назначение размера области просмотра
    #figure управляет шириной, высотой, разрешением и цветом фона диаграммы
    plt.figure(dpi=96, facecolor='g',figsize=(15,8)) #figsize получает кортеж с размера окна программы в дюймах
    point_numbers = list(range(rw.num_points))
    #Вывод точек и отображение диаграммы
    plt.scatter(rw.x_values, rw.y_values,c= point_numbers, cool(point_numbers), edgecolor='none',s=3)
    #Показ в виде линий
    # plt.plot(rw.x_values, rw.y_values, linewidth=2)
    #Выделение первой и последней точек
    plt.scatter(0, 0, c='green', s= 5)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s= 20)
    #Удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    plt.savefig('walking.svg')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
