import dask_cudf
import glob
import cudf
from tqdm import tqdm
import os
import pandas as pd
import dask.dataframe as dd

if __name__ == "__main__":

    seq_df = dask_cudf.read_csv("PeptideManifoldWithOneHotFeatures.csv", blocksize="40MB")
    pysar_parts = glob.glob("PeptideManifoldWithPysarAutocorrelationFeatures_rescaled.csv/*")
    new_dir = "PeptideManifoldWithOneHotFeatures_Split.csv"

    files_done = [i.split("/")[-1] for i in glob.glob(f"{new_dir}/*")]

    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    for file in tqdm(pysar_parts):
        
        file_part = file.split("/")[-1]

        if file_part in files_done:
            print("Skipping")
            continue
    
        df = pd.read_csv(file)

        seq_part = seq_df.loc[seq_df['Sequence'].isin(df['Sequence'])]

        seq_part.to_csv(f"{new_dir}/{file_part}", single_file=True)
