						Introduction:

This repository takes a data set that contains the answers to a 40 question questionaire and does a factor analyis and then clusters those individuals into groups. The factor analysis gets a measure of 6 traits from the questionaire. The personality traits are then used to cluster the individuals into 4 groupsusing the silhouette score as a metric for the goodness of the clustering technique. KMean clustering, Gaussian mixture Model clustering, and Agglomerative Hierarchical clustering techniques are used on the data. The data is then split into 2 subsets that contain United States only responses and Hong Kong only responses to see if the results are different by country. 

						final.py Program

1) Load your data in line 11

2) Set factors in line 22 to the number of questions in the questionaire; plot and analyze the eigen values. Where the values kink or create an elbow is where the optimum number of factos is.

3) Set the number of factors equal to the optimum in line 31 in the FactorAnalyzer machine 

4) The program will run 3 clustering techniques (KMEAN, GMM, and AHC) and return silhouette scores for each of the techniques. 

5) For the AHC technique you will have to look at the Dendrogram to decide on the optimal numbal of clusters for the Agglomerative clustering. 

						compare_countries.py

1) Load your data into line 12

2) Choose the subsets you want to analyze and put those country codes into into lines 15 and 24

3) Set the factors eqaul to the number of questions in lines 32 and 42

4) Analyze each evplot 

5) Place the optimum factors in each factor analyzer in lines 53 and 69 

6) Cluster the data using AHC, use each Dedrogram to decide on the optimum number of clusters and observe the silhouette score

						Final Eaxm Questions:

e) The optimum number of clusters using each of the techniques was 4 

f) We are not bale to answer this question. It is not necessarly possiable to evalute which algorithm is better. Each technique has pros and cons and since we can not vizualize the data in a 2D plane we are not able to see how the technique clusters. This is one of the benefits of the AHC technique. We can use the Dendrogram to help us decide on the optimal number of clusters. We aslo do not have metric to comapre across the clustering techniques. We are able to use the silhouette score to compare within each technique. This way we can see which number of clusters is the best fir for the data. There is also a downside to using KMean and GMM if the data is not clustered around a centroid. In addtion, each of the techniques here the user has to manually input the number of clsuters. If an algorithm like DBSCAN, the compuere would choose the optimal number of clsuters based on the parameters we choose. These technniqes also do not deal wiht noise and must inlcude each data point even if some are outliers. In conclusion, the user must decide which clustering technique is best based on his or her application, the look of the data, and the end result. 

g) My results were differnt for 2 different countries. I choose to analyze the answers from the US and Hong Kong. This was evidnet in the evplot for each country. The US subset very much followed the evplot of the entire sample but the Hong Kong evplot did not have diminishing marginal returns. There was actaully an increase between the b7th and 8th eigen vlaues. This shows that the traits may not be the same for both countries. This is to be expected. Western and eastern countires do not share all the same customs and vlaues. There may also have been a western bias in the questionaire. The 2 countries also had different dedrograms with the US data being much more dense. This could have been from the number of resposnes as the Hong Kong data only had about 80 people where it was over 1500 for the US.  
