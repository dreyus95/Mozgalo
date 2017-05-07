Description:
	This file contains logs describing our weekly meeting progress.


*============================= 02.04.2017. SUNDAY 12:00-16:00 =============================*

- successfully installed Resnet framework for deep learning algorithms

- succesfully installed Torch framework that offers ML algorithms that utilize GPU (Lua language)

- succesfully extracted 2048 features for every image in given dataset

- created script for converting image files to .jpg and .png that Torch accepts


- NEXT MEETING TODO:
	- propose algorithms for unsupervised learning and image classification
	- implement proposed algorithms
	- compare and document results from each classification algorihm



*============================= 09.04.2017. SUNDAY 13:00-17:00 =============================*

- succesfully reduced number of features with PCA algorithm
		- tried with 'mle' : got 627 features reduced set
- tried implementing KMeans and GMM model on reduced set
		- best results so far : 14 clusters
		- still getting 2-3 clusters divided, though they should be same

- NEXT MEETING TODO:
	- try hierarchical grouping algorithm
	- compare and collect results from all tried algorithms
	- fix and document written code
	- find a good visualization tool


*============================= 07.05.2017. SUNDAY 12:00-16:00 =============================*

- initial clustering is done : 10 clusters, 1000 features
- tried out the Wordnet api for classification of clusters by word ( word embeddings)
		- api is working awesome for some clusters,  horrible for others


- NEXT MEETING TODO:
	- try hierarchical clustering for Mozgalo dataset
	- try the model on harder 256 class dataset
	- VISUALIZATION!!!
