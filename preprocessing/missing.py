import pandas as pd
from pandas import DataFrame


def missing_values_counter(df, threshold=0.3) -> DataFrame:
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
    dtype = df.dtypes

    missing_data = pd.concat([total, percent, dtype], axis=1, keys=['Total', 'Percent', "Dtype"]).sort_values("Percent",
                                                                                                              ascending=False)
    missing_data = missing_data[missing_data["Percent"] > threshold]

    print("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"
                                                                                                   "There are " + str(
        missing_data.shape[0]) + f" columns that have missing values above {threshold * 100}%")

    return missing_data


def dropna_rows_below_column_threshold(df,df_miss,threshold=3):
    missing_below_threshold_list = df_miss.iloc[1][df_miss.iloc[1] < threshold].index.tolist()
    df.dropna(subset=[*missing_below_threshold_list])

    return df