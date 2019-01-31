import csv
from matplotlib import pyplot as plt
from datetime import datetime

first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        # print(current_date)
        dates.append(current_date)
        # print(row[0])
        highs.append(int(row[1]))
        lows.append(int(row[3]))
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            # print(row[0])
            highs.append(high)
            lows.append(low)
    # print(highs)
    # Нанесение данных на диаграмму
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=.7)
    plt.plot(dates, lows, c='blue', alpha=.7)
    plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=.3)
    print(dates[0])
    plt.axis([dates[0], dates[-1], min(lows)-3, max(highs)+3])

    # Форматирование диаграммы
    plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=10)
    plt.xlabel('t', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    # plt.tick_params(axis='both', which='major', labelsize=3)
    # plt.plot.cool()

    plt.show()
