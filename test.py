import pandas as pd

# Enable the table_schema option in pandas,
# data-explorer makes this snippet available with the `dx` prefix:
pd.options.display.html.table_schema = True
pd.options.display.max_rows = None

# (Your dataframe here)
iris_filename = './sitka_weather_07-2014.csv'
df1 = pd.read_csv(iris_filename)

df1
