"""

The original dataset can be found here: https://github.com/russian-ad-explorer/russian-ad-datasets/blob/master/json/russian_ads.json

The JSON file is called: "russian_ads.json"

Credit: AndrewBeers

"""

import pandas as pd

#need to cd to location where JSON file is stored

cd C:\Users\Brandon\Downloads

df = pd.read_json (r'C:\Users\Brandon\Download\russian_ads.json')