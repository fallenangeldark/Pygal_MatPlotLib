import json
import pygal
from country_code import get_country_code


# СПИСОК заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# вывод населения каждой страны за 2010год.
wm = pygal.maps.world.World()
wm.title = 'WORLD'
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        cc_populations = {}
        country_name = pop_dict['Country Name']
        population = str(int(float(pop_dict['Value'])))
        code = get_country_code(country_name)
        if code:
            # print(code + ': ' + str(population))
            cc_populations[code] = population
            print(cc_populations)
            wm.add(code, cc_populations)
        else:
            print('Error - ' + country_name)
wm.render_in_browser()
