# How to setup
```
python -m venv data_env
source data_env/bin/activate
pip install matplotlib
python -u "/path/to/file.py" 
```

# What I learnt
How to plot with python, random library and request apis
# Functions
# Part 1
0. Assuming import matplotlib.pyplot as plt
1. plt.plot(array) -> plots the array
2. plt.title("Title", fontsize = size) -> title
3. plt.xlabel("Label", fontsize = size) && plt.ylabel("Label", fontsize = size) -> label x/y
4. plt.tick_params(axis) -> I still have no idea wtf this does
5. plt.scatter(x_values, y_values, c = color, cmap = plt.cm.color) -> plot [x,y] from x and y values, cmap means gradient based on plt.cm.color 
6. plt.figure(figsize = (x, y)) -> plot to x y size 
7. plt.setvisible() -> set something visible / invisible

# Part 2
0. from random import choice
1. choice([a, b, c, d, e, ...]) -> choose a number from a, b, c, d, e, ...
 
# Part 3
0. import requests
1. r = requests.get(url) -> get the API request from some url (r is returned as <Response [200]>)
2. r.status_code -> get the status code
3. r.json -> turns the request json into a python dictionary
