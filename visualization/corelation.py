import numpy as np
import pandas as pd
import seaborn as sns


# TODO : Refactor
# TODO : Pomyśleć jakie ma to mieć funkcjonalności
# TODO : Pomyslec jak to resizować przy dużej ilości zmiennych

class Corelation:

    def __init__(self, df):
        self.__df__ = self.__set_daframe__(df)
        self.__corr__ = self.__compute_corr__()

    def __str__(self):
        print("Corelation class")

    def get_corr(self):
        "return corelation matrix "
        return self.__corr__

    def __set_daframe__(self, df):
        "Check if dataframe is valid"
        if isinstance(df, pd.DataFrame):
            return df
        else:
            raise TypeError("Please provide pandas dataframe")

    def __compute_corr__(self):
        "Compute corelation matrix"
        return self.__df__.corr()

    def __compute_corr_percentage__(self):
        return (np.square(self.__corr__) * 100)

    def __compute_mask__(self):
        "Compute triangled mask for corelation matrix "
        mask = np.zeros_like(self.__corr__, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        return mask


class Heatmap(Corelation):

    def __init__(self, df):
        super(Heatmap, self).__init__(df)
        self.__square__ = False
        self.__line__ = 0.1
        self.__cmap__ = "coolwarm"
        self.__annot__ = True

    def __str__(self):
        return "Heatmap class "

    def get_cmap(self):
        return self.__cmap__

    def get_line(self):
        return self.__line__

    def get_annot(self):
        return self.__line__

    def set_cmap(self,color):
        if isinstance(color, str):
            self.__cmap__=color
        else :
            raise Exception("Color must be string")

    def plot(self, percentage=False, mask=None):

        if percentage:
            self.__corr__ = self.__compute_corr_percentage__()

        if mask:
            mask = self.__compute_mask__()

        heatmap = sns.heatmap(self.__corr__,
                              square=self.__square__,
                              mask=mask,
                              linewidths=self.__line__,
                              cmap=self.__cmap__,
                              annot=self.__annot__)

        return heatmap

