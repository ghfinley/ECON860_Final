import pandas
import numpy
from factor_analyzer import FactorAnalyzer
from sklearn.cluster import KMeans
import matplotlib.pyplot as pyplot
from sklearn.metrics import silhouette_score
import numpy as np 

dataset = pandas.read_csv("dataset_final.csv")  # Load Data Set
dataset.drop(['country'], axis=1,inplace=True)
dataset.drop(['Unnamed: 0'], axis=1,inplace=True)
dataset.replace(0,np.nan, inplace=True) #how do we drop or do we need to drop values = to zero
dataset.dropna(inplace=True)
dataset.to_csv('test.csv')

print(dataset)

# Eigen Values
machine = FactorAnalyzer(n_factors=40, rotation=None)
machine.fit(dataset)
ev,v = machine.get_eigenvalues()
print(ev)

pyplot.scatter(range(1,dataset.shape[1]+1),ev)
pyplot.savefig("evplot.png")

# Using 6 Factors
machine = FactorAnalyzer(n_factors=6, rotation='varimax')
machine.fit(dataset)

loadings = machine.loadings_
numpy.set_printoptions(suppress=True)
print(loadings)
print(machine.get_factor_variance())


dataset = dataset.values 
result = numpy.dot(dataset,loadings)
print(result)


