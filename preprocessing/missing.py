import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

def missing_values_counter(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().mean() * 100).sort_values(ascending=False)
    dtype = df.dtypes

    missing_data = pd.concat([total, percent, dtype], axis=1, keys=['Total', 'Percent', "Dtype"]).sort_values("Percent",
                                                                                                              ascending=False)

    print("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(
        df.shape[0]) + ' Rows.\n''There are ' + str(
        missing_data.shape[0]) + f" columns that have missing values above {threshold * 100}%")

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


