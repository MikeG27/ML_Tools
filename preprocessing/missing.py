import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

def missing_values_counter(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().mean() * 100).sort_values(ascending=False)
    dtype = df.dtypes

    missing_data = pd.concat([total, percent, dtype], axis=1, keys=['Total', 'Percent', "Dtype"]).sort_values("Percent",
                                                                                                              ascending=False)

    print("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(
        df.shape[0]) + ' Rows.\n''There are ' + str(
        missing_data.shape[0]))

    return missing_data


def missing_imputer(df, columns, strategy="most_frequent"):
    """
    :param df: Pandas dataframe
    :param columns: target columns for imputer
    :param strategy: Imputation strategy

    If “mean”, then replace missing values using the mean along each column. Can only be used with numeric data.
    If “median”, then replace missing values using the median along each column. Can only be used with numeric data.
    If “most_frequent”, then replace missing using the most frequent value along each column. Can be used with strings or numeric data.
    If “constant”, then replace missing values with fill_value. Can be used with strings or numeric data.

    :return: imputer instance
    """
    imputer = SimpleImputer(missing_values=np.nan, strategy=strategy)
    df[columns] = imputer.fit_transform(df[columns])
    return imputer

def knn_imputer(df,columns,neighbours = 2):
    """
    Imputation for completing missing values using k-Nearest Neighbors.
    Each sample’s missing values are imputed using the mean value from n_neighbors nearest neighbors found in the training set.
    Two samples are close if the features that neither is missing are close.
    """
    imputer = KNNImputer(n_neighbors=neighbours)
    df[columns] = imputer.fit_transform(df[columns])
    return imputer
