import matplotlib.pyplot as plt
import pygal
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,edgecolors='none',c=y_values,cmap=plt.cm.cool, s=40)

# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Назначение размера шрифта делений на осях.
plt.axis([-100, 1100, -100, 1100000])
plt.show()
