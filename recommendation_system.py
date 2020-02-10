'''
some oddy recommendation algorithm
'''

import pandas as pd
import numpy as np
from pandas import ExcelWriter
import glob
import datetime
from collections import Counter
from itertools import combinations


### main catalog initiate
catalog = {}


### functions
dateparse = lambda x: pd.datetime.strptime(x, "%d.%m.%Y %H:%M:%S")


def adopttocal(art):
    #########################################################################
    # function builds dictionary of Counters.                               #
    # key is the item and the value is counter in which                     #
    # it counts all the occurences with other items                         #
    # then, getting the item(art, name, or whatever) by key                 #
    # you will get the Counter (sorted by number of occurences eventually)  #
    # with all the recommended items                                        #
    # NOTE: to collect this dict it requires the big datasets               #
    #########################################################################
    for item in art:
        if item in catalog.keys():
            temp = catalog[item]
            for item_2 in art:
                if item_2 != item: # exclude self counting
                    temp[item_2] += 1
        else:
            temp = Counter()
            for item_2 in art:
                if item_2 != item: # exclude self counting
                    temp[item_2] += 1
            catalog[item] = temp


pd.set_option('display.max_columns', 10)            # output tewaks
pd.set_option('display.width', 1000)                # output tewaks


# importing sales excel files
files = glob.glob("datasets/sl*.xlsx")
frames = []
for f in files:
    df = pd.read_excel(
        f,
        usecols=[1, 2],
        skiprows=7,
        index_col=0,
        parse_dates=True,
        date_parser=dateparse,
    )
    df.columns = ['art']
    df.index.name = 'date'
    frames.append(df)
sales = pd.concat(frames, axis=0, sort=False)

sales['timestamp'] = sales.index.astype(int) / 10**9

print(sales.head())
sales.groupby(by='timestamp')['art'].apply(list).map(adopttocal)

# you can fetch by item name, but here we are fetching just for example by number of key
art_number = 5
print('\nTop {} recommended items for '.format(str(art_number)), list(catalog.keys())[5], ':')
# print('\n', catalog[list(catalog.keys())[5]].most_common(5))
for art, _ in catalog[list(catalog.keys())[5]].most_common(5):
    print(art)

# most frequent pairs of goods
count = Counter()
arts = sales.groupby(by='timestamp')['art'].apply(list)

for sublist in arts:
    count.update(Counter(combinations(sublist, 2)))

most_populars = 10
print(f'\n{most_populars} most popular goods pairs: ')
for i in range(0, most_populars):
    print(count.most_common(most_populars)[i][0], ' : number of occurences = ', count.most_common(most_populars)[i][1])