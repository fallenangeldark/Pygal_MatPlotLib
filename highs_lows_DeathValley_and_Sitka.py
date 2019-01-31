import csv
from matplotlib import pyplot as plt
from datetime import datetime

# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)
datesSitka, highsSitka, lowsSitka, datesDeath, highsDeath, lowsDeath = [], [], [], [], [], []
filename1 = 'sitka_weather_2014.csv'
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        # print(current_date)
        datesSitka.append(current_date)
        highsSitka.append(int(row[1]))
        lowsSitka.append(int(row[3]))
filename2 = 'death_valley_2014.csv'
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            datesDeath.append(current_date)
            # print(row[0])
            highsDeath.append(high)
            lowsDeath.append(low)
    # print(highs)
    # Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(datesSitka, highsSitka, c='red', alpha=.8)
plt.plot(datesSitka, lowsSitka, c='blue', alpha=.8)
plt.plot(datesDeath, highsDeath, c='green', alpha=.9)
plt.plot(datesDeath, lowsDeath, c='orange', alpha=.9)
plt.fill_between(datesSitka, highsSitka, lowsSitka, facecolor='yellow', alpha=.5)
plt.fill_between(datesDeath, highsDeath, lowsDeath, facecolor='green', alpha=.5)
# print(dates[0])
# plt.axis([dates[0], dates[-1], min(lowsSitka)-3, max(highsDeath)+3])

# Форматирование диаграммы
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=10)
plt.xlabel('t', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=3)
# plt.plot.cool()

plt.show()
