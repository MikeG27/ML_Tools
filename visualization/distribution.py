import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import probplot
from statsmodels.distributions.empirical_distribution import ECDF

sns.set()

def ecdf(df_feature,xlabel):
    ecdf = ECDF(df_feature)
    plt.title("ECDF Plot ")
    plt.plot(ecdf.x, ecdf.y)
    plt.xlabel(xlabel)
    return ecdf


def distribution(df_feature,xlabel):
    bins = int(np.sqrt(len(df_feature)))
    df_feature.hist(bins=bins)
    plt.title("Histogram")
    plt.xlabel(xlabel)


def box_plot(df_feature):
    df_feature.plot.box()
    plt.title("Boxplot")

def probability_plot(df_feature):
    probplot(df_feature, plot=plt)


def distribution_analyzer(df_feture,title):
    plt.figure(figsize=(13,7))


    plt.suptitle("{} distribution analyzer".format(title))

    plt.subplot(2, 2, 1)
    distribution(df_feture,title)
    plt.text(1, 1, "LOL", ha='right', rotation=-15, wrap=True)

    plt.subplot(2, 2, 2)
    ecdf(df_feture,title)

    plt.subplot(2, 2, 3)
    box_plot(df_feture)

    plt.subplot(2, 2, 4)
    probability_plot(df_feture)

    plt.tight_layout()
    plt.show()
