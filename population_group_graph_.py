import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from country_code import get_country_code


# СПИСОК заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# вывод населения каждой страны за 2010год.
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            # print(code + ': ' + str(population))
            cc_populations[code] = population
        else:
            print('Error - ' + country_name)

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 50000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336688', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'WORLD Population in 2010'
wm.add('0-50m', cc_pops_1)
wm.add('50m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_in_browser()
    # wm.add('2010', [code, population])

# wm = pygal.maps.world.World()
# wm.title = 'North, Central, and South America'
# print(cc_populations)
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr',  'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#     'gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.add('2010',  cc_populations)
# for code, popul in cc_populations.items():
#     wm.add('2010', (code, popul))
