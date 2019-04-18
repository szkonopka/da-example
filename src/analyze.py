import traceback
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

RESULT_FILE = '../data/result.txt'

def add_to_file(txt, filename):
    with open(filename, 'a') as file:
        file.write(txt + '\n\n')

def show_statistics(df, headers, name):
    print("{} statistics".format(name))
    add_to_file("{} statistics".format(name), RESULT_FILE)
    num_bins = 10
    for header in headers:
        print('\n{}'.format(header))
        print(df[header].value_counts(normalize=True))
        add_to_file(df[header].value_counts(normalize=True).to_string(), RESULT_FILE)

def show_plot(first_df, second_df, header, num_bins):
    plt.hist(first_df[header], num_bins, density=1, facecolor='black', alpha=0.5)
    plt.hist(second_df[header], num_bins, density=1, facecolor='red', alpha=0.5)
    handles = [Rectangle((0, 0), 1, 1, color=c, ec="k", alpha=0.5) for c in ['black', 'red']]
    labels = ["DC", "Marvel"]
    plt.legend(handles, labels)
    plt.show()

def main():
    dc_df = pd.read_csv('../data/dc_heroes.csv')
    marvel_df = pd.read_csv('../data/marvel_heroes.csv')

    # cleaning the datasets
    print("DC heroes (before cleaning): {}".format(dc_df.size))
    print("Marvel heroes (before cleaning): {}".format(marvel_df.size))

    print(dc_df.describe(include='all'))
    print(marvel_df.describe(include='all'))

    add_to_file("DC heroes (before cleaning): {}".format(dc_df.size), RESULT_FILE)
    add_to_file(dc_df.describe(include='all').to_string(), RESULT_FILE)

    add_to_file("Marvel heroes (before cleaning): {}".format(marvel_df.size), RESULT_FILE)
    add_to_file(marvel_df.describe(include='all').to_string(), RESULT_FILE)

    headers = [
        'id',
        'sex',
        'gsm',
        'align',
        'eye',
        'hair',
        'alive'
    ]

    show_statistics(dc_df, headers, 'DC')
    show_statistics(marvel_df, headers, 'Marvel')
    show_plot(dc_df, marvel_df, 'year', 100)

try:
    main()
except Exception as ex:
    print(traceback.format_exc())
finally:
    print("Program stops")
