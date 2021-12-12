						Introduction:

This repository takes a data set that contains the answers to a 40 question questionaire and does a factor analyis and then clusters those individuals into groups. The factor analysis gets a measure of 6 traits from the questionaire. The personality traits are then used to cluster the individuals into 4 groupsusing the silhouette score as a metric for the goodness of the clustering technique. KMean clustering, Gaussian mixture Model clustering, and Agglomerative Hierarchical clustering techniques are used on the data. The data is then split into 2 subsets that contain United States only responses and Hong Kong only responses to see if the results are different by country. 

						final.py Program

1) Load your data in line 11

2) Set factors in line 22 to the number of questions in the questionaire; plot and analyze the eigen values. Where the values kink or create an elbow is where teh optimum number of factos is.

3) Set the number of factors equal to the maximum in line 31 in the FactorAnalyzer machine 

4) 
