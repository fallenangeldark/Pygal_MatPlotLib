import json
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Создание вызова API и сохранение ответа.
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
filename = 'python_stars.json'
# with open(filename, 'w', encoding='utf-8') as f:
#     f.write(json.dumps(r.json(), indent=4))
# print('Status code: ', r.status_code)

# сохранение ответа API в переменной.
with open(filename, 'r') as f:
    response_dict = json.load(f)
# response_dict = r.json()

# print(response_dict['items'])
print("Total repositories:", response_dict['total_count'])

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
names, plot_dicts = [], []
# print("Repositories returned:", len(repo_dicts))
# print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    label_new = repo_dict['description']
    # if isinstance(label_new, str):
    #     lavel_new = label_new.encode('ascii','ignore').decode('ascii').encode('utf-8').decode('utf-8')
    #     plot_dict = {
    #     'value': repo_dict['stargazers_count'],
    #     'label':label_new,
    #     }
    # elif label_new is None:
    #     plot_dict = {
    #     'value': repo_dict['stargazers_count'],
    #     'label':repo_dict['owner']['login'],
        # }
    if label_new is None:
        label_new = 'No description'
        # print(label_new)
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': label_new,
            'xlink': repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)
    else:
        label_new = label_new.encode('ascii','ignore').decode('ascii').encode('utf-8').decode('utf-8')
        # print(label_new, '\n')
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': label_new,
            'xlink': repo_dict['html_url']
        }
        plot_dicts.append(plot_dict)

print(plot_dicts)
my_style = LS('#336699', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = True  # Показывает легенду (квадраты слева от графика)
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 60  # для сокращения длинных имен меток, размер меток, если текст не влазит то он сокращается
my_config.show_y_guides = False  # задает пунктирные метки по оси У
my_config.width = 1000  # Ширина графика

chart = pygal.Bar(my_config, style=my_style)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_in_browser()

# Анализ первого репозитория
# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])
# repo_dict = repo_dicts[1]
# print('\nKeys:', len(repo_dict))
# print("\nSelected information about second repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# for key in sorted(repo_dict.keys()):
#     print(key)
# #     pass

# Обработка результатов.
# print(response_dict.keys())
