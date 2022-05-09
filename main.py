import scraper
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from scipy import stats
from sys import argv


remove_outliners = False


def main():
    if scraper.CSV_NAME in os.listdir(os.getcwd()):
        print("CSV file already created")
    else:
        print("Creating CSV file")
        scraper.generate_CSV()

    table = pd.read_csv(os.path.join(os.getcwd(), scraper.CSV_NAME))

    if remove_outliners:
        table = table[table["Land"] < 5E6]

    max_value = table["Land"].max()
    fig, ax = plt.subplots(figsize = (7, 7))

    x = table['Land']
    y = table['HDI']
    ax.set_xlabel("Land (km²)")
    ax.set_ylabel("HDI")
    ax.set_title("Countries by land and HDI")

    ax.scatter(x, y, s=40, alpha=0.8, edgecolors="k")

    # linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    ax.plot([0, max_value], [intercept, intercept + slope * max_value], color="green")
    print(f"r² = {pow(r_value,2)}")
    plt.show()


if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1] == '1':
            remove_outliners = True
    main()