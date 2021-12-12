import pandas
import numpy
from factor_analyzer import FactorAnalyzer
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as pyplot
from sklearn.metrics import silhouette_score
import numpy as np 
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

dataset = pandas.read_csv("dataset_final.csv")  # Load Data Set
dataset.drop(['country'], axis=1,inplace=True)
dataset.drop(['Unnamed: 0'], axis=1,inplace=True)
dataset.replace(0,np.nan, inplace=True) #how do we drop or do we need to drop values = to zero
dataset.dropna(inplace=True)
dataset.to_csv('test.csv')

#print(dataset)

# Eigen Values
machine = FactorAnalyzer(n_factors=40, rotation=None)
machine.fit(dataset)
ev,v = machine.get_eigenvalues()
#print(ev)

pyplot.scatter(range(1,dataset.shape[1]+1),ev)
pyplot.savefig("evplot.png")

# Using 3 Factors
machine = FactorAnalyzer(n_factors=3, rotation='varimax')
machine.fit(dataset)

loadings = machine.loadings_
numpy.set_printoptions(suppress=True)
#print(loadings)
#print(machine.get_factor_variance())


dataset = dataset.values 
result = numpy.dot(dataset,loadings)
#print(result)
#print(result.shape)

data = result

                       #Cluster with the Characteristics 

# KMean
print("KMean")
def run_kmeans(n,data): #now we have a funtion that we can run multiple times with differnt clusters 

	machine = KMeans(n_clusters=n) #construct machine
	machine.fit(data) #fit the data
	machine.predict(data) #asign a number to the data poins 
	results = machine.predict(data)
	if n>1:
		print(silhouette_score(data, machine.labels_, metric = 'euclidean'))  #Silhoutte Score


kmeans_silhouette = [run_kmeans(i+1,data) for i in range(7)] 

# The optimal number of clusters is 4 based on Silhouette Score

#GMM
print("GMM")
def run_gmm(n, data):
	gmm_machine = GaussianMixture(n_components=n)
	gmm_results = gmm_machine.fit_predict(data)
	silhouette = 0
	if n > 1:
		silhouette = (silhouette_score(data, gmm_results, metric = 'euclidean'))
		print(silhouette)
	return silhouette

gmm_silhouette_list = [ run_gmm(i+1, data) for i in range(7)]
print(gmm_silhouette_list)

# The optimal number of clusters is 3 based on Silhouette Score

#AHC
pyplot.title("Dendrogram")
dendrogram_object = shc.dendrogram(shc.linkage(data, method = "ward")) 
pyplot.savefig("dendrogram.png")
pyplot.close()
  
machine = AgglomerativeClustering(n_clusters = 4, affinity="euclidean", linkage="ward")
results_ahc_us = machine.fit_predict(data) 

silhouette = (silhouette_score(data, results_ahc_us, metric = 'euclidean'))
print(silhouette)











