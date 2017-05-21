This is the implementation of the Mozgalo task. Dataset of features is loaded with torchfile library, which knows how to load already extracted features inside xxx.t7 file that contains the results of feature extraction done by Torch.

PCA is used to reduce the high dimensionality(Torch output is 2048 features per example image), and remove potential linear correlation between features.

As an optimal clustering method it was decided for GMM to be used.

All rights reserved © FerKani

Goran Brlas

Josip Silović

Nikola Mrzljak

Franjo Matković
