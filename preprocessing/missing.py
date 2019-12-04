import pandas as pd


def missing_values_counter(df, threshold=0.3):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum() / df.isnull().count() * 100).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    missing_data = missing_data[missing_data["Percent"] > threshold]

    print("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) +
          " Rows.\n""There are " + str(missing_data.shape[0]) + f" columns that have missing values above {threshold * 100}%")

    return missing_data