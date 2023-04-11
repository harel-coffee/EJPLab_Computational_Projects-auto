import pandas as pd
import dask.dataframe as dd
from dask.array.slicing import shuffle_slice
import numpy as np

np.random.seed(420)

if __name__ == "__main__":

    real_columns = ['Sequence']
    numbers = [i for i in range(121)]
    real_columns += numbers

    df = dd.read_csv("PeptideManifoldWithOneHotFeatures.csv", blocksize="100MB").reset_index()
    df.columns = real_columns
    df = df.drop(120, axis=1)

    mutants_in_test = pd.read_csv("Dataset.csv")['name'].to_list()

    mutant_test = df.loc[df['Sequence'].isin(pd.Series(mutants_in_test))].compute()
    df = df.loc[~df['Sequence'].isin(mutants_in_test)]

    df_10 = df.sample(frac=0.1)
    df = df.loc[~df['Sequence'].isin(df_10['Sequence'].compute())]

    d_arr = df.to_dask_array(True)
    df_len = len(df)
    index = np.random.choice(df_len, df_len, replace=False)
    d_arr = shuffle_slice(d_arr, index)
    df = d_arr.to_dask_dataframe(df.columns)

    df_10.to_csv("Validation_Set",header=None, index=None)
    df.to_csv("Training_Set", header=None, index=None)
    mutant_test.to_csv("Testing_Set", header=None, index=None)
