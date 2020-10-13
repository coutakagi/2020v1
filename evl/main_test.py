'''
Created on 2020/10/03

@author: Takagi
'''
print("start evaluation")
import os

# change following folder names
mainpath="./data/"
outputfol="./result/"
if not os.path.exists(outputfol):
    os.mkdir(outputfol)


###
singlefilename=mainpath+"set1/result_matrix.csv"

outputfilename_distribution=outputfol+"result_distribution.csv"
outputfilename_cluster=outputfol+"result_cluster.csv"
#distribution/cluster data size for plot
dist_size=100
cluster_size=100

#create file list (single file example)
filenames=[singlefilename]


from sequence import exe_distribution
exe_distribution(filenames,outputfilename_distribution, dist_size)

from sequence import exe_clustersize
exe_clustersize(filenames,outputfilename_cluster, cluster_size)


