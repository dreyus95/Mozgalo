All rights reserved © FerKani

Goran Brlas

Josip Silović

Nikola Mrzljak

Franjo Matković


# MOZGALO COMPETITION

## Project theme: Unsupervised clustering of a given dataset

Project is written in Python 3 using Resnet framework for feature extraction. We have decided for [Torch](http://torch.ch/blog/2016/02/04/resnets.html) implementation due to its CUDA principles. 
Instructions on how to setup everything can be found bellow.

## Table of contents

<a href="#Req">Requirements</a><br>
<a href='#Packages'>Packages and installation</a><br>
<a href='#Usage'>Using Torch</a><br>
<a href='#Results'>Results</a><br>

## Requirements
<a id='Req'></a>


```
Python 3
```
```
CUDA capable machine (Unix/Linux is recommended) -> NVIDIA GPU
Jupyter Notebook
```


## Packages and installation
<a id='Packages'></a>


If you don't have an NVIDIA GPU then you will not be able to run this model for feature extraction.
Luckily, we have already extracted and pushed the features for our given dataset in the repository.
To use the code we suggest not having the virtual environment, but pure Unix/Linux.  
  
1.	To install Torch follow the instructions on [this](http://torch.ch/docs/) link.

2.	Next, install CudNN library from [this](https://developer.nvidia.com/cudnn) link following the exact instructions.

3.	You will also need [this](https://github.com/soumith/cudnn.torch/tree/R4) addition for the CudNN lib.

4.	The model we have chosen is ResNet-200, which can be download from [this](https://d2j0dndfm35trm.cloudfront.net/resnet-200.t7) link.

5.	To load features.t7 file from torch, you can simply install torchfile notebook using: pip install torchfile

6.	For word embedding we used the NLTK framework which contains WordNet database of english words and their connections.
	Install it using : sudo pip install -U nltk



## Using Torch
<a id='Usage'></a>


Before doing anything, it is required that all images from dataset are in PNG format.
We have provided a simple convertImageFormat.py script to do so. Make sure you position your dataset in the right directory
as it is written inside the script and run it.

To extract images use the next command:

```
features.lua resnet-200.t7 path_to_pic

features.lua resnet-200.t7 *    (for all pictures in dataset dir)
```

After this you get the features.t7 file with all features.
Size of feature vectors is 2048x1.
To classify pictures(used for word embedding) use the following command:

```
th classify.lua resnet-200.t7 path_to_pic
```

You can see our implementation of word embeddings inside UnsupervisedImageClassifier.ipynb notebook and the results it yielded.



## Results
<a id='Results'></a>


As you can see inside our UnsupervisedImageClassifier.ipynb notebook, we have decided to use [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) for dimensional reduction.
We have reduced from 2048 to 1000 features per image. The number was decided by trial and error method, visually it provided us
wih the best result. The number of clusters we chose was 10, as it also visually gave us the most reasonable choice. You are free to experiment
with the numbers so you can see what suits your wishes for clustering best.

We have also tried the model on a harder dataset, which you can see in our UnsupervisedLearningHarderDatasetGMM.ipynb notebook.
You can see how well the model works on a labeled dataset, as we used the Adjusted Rand Index to verify how good our cluster
predictions are in contrast to the real results.


