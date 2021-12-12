import pandas
import numpy
import numpy as np 
from factor_analyzer import FactorAnalyzer
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as pyplot
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

df = pandas.read_csv("dataset_final.csv")  # Load Data Set

# US Subset
df_us = df.loc[df['country'] == "US"]
df_us.drop(['country'], axis=1,inplace=True)
df_us.drop(['Unnamed: 0'], axis=1,inplace=True)
df_us.replace(0,np.nan, inplace=True) #how do we drop or do we need to drop values = to zero
df_us.dropna(inplace=True)

#print(df_us)

# Hong Kong Subset
df_hk = df.loc[df['country'] == "HK"]
df_hk.drop(['country'], axis=1,inplace=True)
df_hk.drop(['Unnamed: 0'], axis=1,inplace=True)
df_hk.replace(0,np.nan, inplace=True) #how do we drop or do we need to drop values = to zero
df_hk.dropna(inplace=True)
#print(df_hk)

# Eigen Values - US
machine = FactorAnalyzer(n_factors=40, rotation=None)
machine.fit(df_us)
ev_US,v = machine.get_eigenvalues()
#print(ev_US)

pyplot.scatter(range(1,df_us.shape[1]+1),ev_US)
pyplot.savefig("evplot_US.png")


# Eigen Values - HK
machine = FactorAnalyzer(n_factors=40, rotation=None)
machine.fit(df_hk)
ev_HK,v = machine.get_eigenvalues()
#print(ev_HK)

pyplot.scatter(range(1,df_hk.shape[1]+1),ev_HK)
pyplot.savefig("evplot_HK.png")



# Using 6 Factors - US - 6 Factors chose based on eigen value elbow analysis
machine = FactorAnalyzer(n_factors=6, rotation='varimax')
machine.fit(df_us)

loadings = machine.loadings_
numpy.set_printoptions(suppress=True)
#print(loadings)
#print(machine.get_factor_variance())


df_us = df_us.values 
result = numpy.dot(df_us,loadings)
#print(result)
#print(result.shape)

## For HK it is harder to choose the appropote number of factors, we do not have a diminsihing marginal returns. 

machine = FactorAnalyzer(n_factors=10, rotation='varimax')
machine.fit(df_hk)

loadings = machine.loadings_
numpy.set_printoptions(suppress=True)
#print(loadings)
#print(machine.get_factor_variance())


df_hk = df_hk.values 
result = numpy.dot(df_hk,loadings)
#print(result)
#print(result.shape)

## Compare the Analysis with AHC Clustering 

#AHC - US
print("US AHC silhouette score")
pyplot.title("Dendrogram_US")
dendrogram_object = shc.dendrogram(shc.linkage(df_us, method = "ward")) 
pyplot.savefig("dendrogram_US.png")
pyplot.close()
#Optimum # is 4 from the Dendrogram
machine = AgglomerativeClustering(n_clusters = 4, affinity="euclidean", linkage="ward")
results_ahc_us = machine.fit_predict(df_us)

silhouette = (silhouette_score(df_us, results_ahc_us, metric = 'euclidean'))
print(silhouette)


# AHC - HK
print("HK AHC silhouette score")
pyplot.title("Dendrogram_HK")
dendrogram_object = shc.dendrogram(shc.linkage(df_hk, method = "ward")) 
pyplot.savefig("dendrogram_HK.png")
pyplot.close()
#Optimum # is 4 from the Dendrogram
machine = AgglomerativeClustering(n_clusters = 4, affinity="euclidean", linkage="ward")
results_ahc_hk = machine.fit_predict(df_hk)

silhouette = (silhouette_score(df_hk, results_ahc_hk, metric = 'euclidean'))
print(silhouette)







