import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from visualization.correlation import Heatmap
from visualization.distribution import distribution_analyzer


def check_distribution(df):
    # descriptive statistics summary
    feature = df['SalePrice']
    distribution_analyzer(feature,"SalePrice")
    #ecdf(feature)

def check_corelation(df):
    df = df[df.columns[0:20]]  # get first ten columns
    heatmap = Heatmap(df)
    print(heatmap)
    heatmap.set_cmap("RdBu")
    heatmap.plot()
    plt.show()



if __name__ == "__main__" :
    df = pd.read_csv("../train.csv")
    check_distribution(df)
    #
    # import numpy as np
    # import matplotlib.pyplot as plt
    #
    # np.random.seed(19680801)
    #
    # fig, ax = plt.subplots()
    # x = 30 * np.random.randn(10000)
    # mu = x.mean()
    # median = np.median(x)
    # sigma = x.std()
    # textstr = '\n'.join((
    #     r'$\mu=%.2f$' % (mu,),
    #     r'$\mathrm{median}=%.2f$' % (median,),
    #     r'$\sigma=%.2f$' % (sigma,)))
    #
    # ax.hist(x, 50)
    # # these are matplotlib.patch.Patch properties
    # props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    #
    # # place a text box in upper left in axes coords
    # ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
    #         verticalalignment='top', bbox=props)
    #
    # plt.show()

    #check_corelation()



