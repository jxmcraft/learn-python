import matplotlib.pyplot as plt # graphs
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS # bar charts
from random import choice, randint
import requests
# squares = [x**3 for x in range(5000)]
# plt.plot(squares, linewidth=5)
# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# # plt.tick_params(axis='both', labelsize=14)
# plt.set_cmap(plt.cm.Blues)
# plt.show()

class RandomWalk():
    def __init__(self, steps = 5000):
        self.steps = steps
        self.x = 0
        self.y = 0
        self.dir = [1, -1]
        self.mag = [1,2,3,4,5,6]
        self.y_route = [0]
        self.x_route = [0]
    
    def walk(self, x, y):
        self.x = self.x_route[-1] + x
        self.y = self.y_route[-1] + y
        self.x_route.append(self.x)
        self.y_route.append(self.y)

    def rando(self):
        for i in range(self.steps):
            self.walk(choice(self.dir) * choice(self.mag), choice(self.dir) * choice(self.mag))
    
    def visWalk(self):
        self.rando()
        points_number = list(range(len(self.x_route)))
        plt.scatter(self.x_route, self.y_route, c = points_number, cmap=plt.cm.Blues)
        plt.show()

class Die():
    def __init__(self, side = 6):
        self.side = side

    def roll(self):
        # self.history.append(choice(range(self.side) + 1))
        return randint(1, self.side)
    
class API():
    def __init__(self, url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'):
        self.url = url
        self.names = []
        self.stars = []

        response_dict = requests.get(self.url).json()
        repo_dicts = response_dict['items']
        for repo_dict in repo_dicts:
            self.names.append(repo_dict['name'])
            self.stars.append(repo_dict['stargazers_count'])
    
    def showChart(self):
        my_style = LS('#333366', base_style=LCS)
        chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
        chart.title = 'Most-Starred Python Projects on GitHub'
        chart.x_labels = self.names
        chart.add('', self.stars)
        chart.render_to_file('python_repos.svg')
    
if __name__ == "__main__":
    # Part 3 API

    current = API()
    current.showChart()
    # url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    # r = requests.get(url)
    # print(r)
    # print("Status code:", str(r.status_code))
    # response_dict = r.json()
    # print(response_dict.keys())
    # print(response_dict["total_count"])
    # print(response_dict["incomplete_results"])
    # print(response_dict["items"])
    # first = response_dict['items'][0]
    # print(first.keys())
    # print(first['owner']['login'])


    # Part 1 Random Walk + Scatter
    # vis = RandomWalk()
    # vis.visWalk()

    # Part 2 Die + Barchart
    # die = Die()
    # history = []
    # frequencies = [0,0,0,0,0,0]
    # for i in range(1000):
    #     roll = die.roll()
    #     history.append(roll)
    #     frequencies[roll-1] += 1
    
    # hist = pygal.Bar()
    # hist.x_labels = ["1", "2", "3", "4", "5", "6"]
    # hist.x_title = "Results"
    # hist.y_title = "Frequencies"
    # hist.add("D6", frequencies)
    # hist.render_to_file('die_visual.svg')

    

# skipping the boring stuff and going directly into API
