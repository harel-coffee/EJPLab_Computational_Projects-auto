# Autoencoders  

This folder contains the nescessary files for training the autoencoders. The datasets used for training these autoencoders are 10's of GB in size.

## Scripts for Generating Dataset
If you want to create them locally, use the following scripts:  

Compute_OneHot_Features.py - Generates one-hot encodings for the 6-mer sequences. (DL_Pytoch)
Compute_Pysar_Features.py - Generates PySAR features for 6-mer sequences. Excuted with the wrapper file. (DL_Pytoch)  
DASK_StandardScaler.py - Scales data generated from previous two scripts. (DL_Pytoch)  
RemoveRedundantColumns.py - Needs to be found. (DL_Pytoch)
create_train_val_test_with_shuffle.py - Splits the array into training, validation, and testing using dask for pySAR features. WARNING: Parameter for parition size may need to be adjusted based on computer specifications. (DL_Pytoch)  
split_one_hot_encodings.py - Splits the sequence datasets into the same order as the pySAR datasets. (DL_Pytoch)  
check_sets.py - Checks if the Sequence set and pySAR set are of same length. (DL_Pytoch)  

The following peptide was removed: "NAAAAA" for incompatibility with pandas.

## Scripts for Tuning Autoencoders
Autoencoders were trained using a custom generate_arrays_from_file function. This function reads the DASK generated files into memory and yields numpy arrays for training.  
To train the autoencoders, use the following scripts:  

Peptide_Autoencoder_HT_Seq.py - Trains a sequence autoencoder on peptide manifold. (DL_TFGPU)
Peptide_Autoencoder_Pysar_HT.py - Trains a pySAR autoencoder on peptide manifold. (DL_TFGPU)

## Scripts for Visualization  
Cluster_Seq_pysar_Manifold_RAPIDS_Kmeans.py - Combines the sequence and pySAR manifolds and performs kmeans clustering. Generates manifold figure. Splits datasets into testing and training. (RAPIDS)  
Make_Embedding_Figures.py - Makes UMAP embeddings for sequence and pySAR manifolds separately. (RAPIDS) 

## Optuna Studies  
Optuna study objects are provided. They hold information on optimization history and best parameters. They are held in the following files:  
Pysar_Study.pickle  
Seq_Study.pickle  

