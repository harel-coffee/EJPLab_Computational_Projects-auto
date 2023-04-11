import cudf
import glob
from tqdm import tqdm
if __name__ == "__main__":

    pysar_dir = "PeptideManifoldWithPysarAutocorrelationFeatures_rescaled.csv"
    seq_dir = "PeptideManifoldWithOneHotFeatures_Split.csv"

    pysar_files = glob.glob(f"{pysar_dir}/*")
    seq_files = glob.glob(f"{seq_dir}/*")

    for idx, seq_file in enumerate(tqdm(seq_files)):
        
        seq_df = cudf.read_csv(seq_file)
        pysar_df = cudf.read_csv(pysar_files[idx])

        len_seq = seq_df.__len__()
        len_pysar = pysar_df.__len__()

        if len_seq != len_pysar:
            print(seq_file)

            missing_data = pysar_df.loc[~pysar_df['Sequence'].isin(seq_df['Sequence'])]
            print(missing_data)
    