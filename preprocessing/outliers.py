import numpy as np
from scipy import stats


def remove_outliers_STD(df, treshold=3):
    """
    Remove preprocessing from pandas dataframe based on standard deviation indicator.
    :param df: Pandas dataFrame
    :param treshold: standard deviation treshold
    :return df_out : Pandas dataframe without preprocessing
    """
    z = np.abs(stats.zscore(df))
    df_out = df[(z < treshold).all(axis=1)]
    print("Removed {} rows based on STD ".format(df.shape[0] - df_out.shape[0]))
    return df_out


def remove_outliers_IQR(df, IQR_mul=1.5):
    """
    Remove preprocessing from pandas dataframe based on IQR indicator.
    :param df: Pandas dataFrame
    :param IQR_mul : IQR_mult > 1.5 - normal preprocessing, IQR_mul > 3 - extreme preprocessing
    :return df_out :
    """
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_outliers = df < (Q1 - IQR_mul * IQR)
    upper_outliers = df > (Q3 + IQR_mul * IQR)
    df_out = df[~((lower_outliers) | (upper_outliers)).any(axis=1)]
    print("Removed {} rows based on IQR".format(df.shape[0] - df_out.shape[0]))
    return df_out
