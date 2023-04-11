# Anaconda Environments  
## Machine Learning  
There will be three total enviorments to run all scripts found in this repository. One for training models using the transformers library, and the other for visualizations of plots. The machine learning environment can be created from the DL_Pytorch.yml file in this folder with the following command:  

conda env create -f DL_Pytorch.yml  

For the Tensorflow enviorment for running the autoencoders (DL_TFGPU):

conda env create -f DL_TFGPU.yml  

## Visualizations  
The visualization enviorment uses RAPIDS and can not be created directly from a yml file. Here is a list of the relavent python libraries with their versions.  
To install rapids, please copy the command from the following link. We used version 23.02 with cuda 11.2:

https://docs.rapids.ai/install?_gl=1*1ddpnh3*_ga*NjU4OTMxMjk4LjE2Nzk1ODM5MDk.*_ga_RKXFW6CM42*MTY4MTIzMzg4MC40LjEuMTY4MTIzMzkwNi4wLjAuMA..#selector

After running this command, you can install the nescessary libraries given listed here:  

  - matplotlib-base=3.7.1=py310he60537e_0
  - scipy=1.10.1=py310h8deb116_0  
  - seaborn=0.12.2=hd8ed1ab_0  
  - scikit-learn=1.2.2=py310h209a8ca_0  
  - ipython=8.11.0=pyh41d4057_0  
  - pandas=1.5.3=py310h9b08913_0  
  - numpy=1.23.5=py310h53a5b5f_0  
  - tqdm=4.65.0=pyhd8ed1ab_1  
  - optuna=3.1.0=pyhd8ed1ab_0  

