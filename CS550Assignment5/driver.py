'''
Created on Apr 15, 2018
file: driver.py
@author: mroch, Alexander Giang
'''
from ml_lib.learning import (DataSet, 
                             DecisionTreeLearner, NeuralNetLearner)
from std_cv import cross_validation
from random import shuffle

from copy import deepcopy
    
def shuffle_data(dataset):
    shuffle(dataset.examples)   

def learn(dataset):
    '''Given a dataset, create a shuffled copy of the data. Run a 10 fold
    cross validation (std_cv.cross_validation) using decision trees and neural
    nets (DecisionTreeLearner and NeuralNetLearner). The data are only
    shuffled once, so that std_cv.cross_validation will use the same exact
    training and test data on each of the folds for both learners.'''
    shuffle_data(dataset)   
    cv_tree = cross_validation(DecisionTreeLearner,dataset)
    dataset.attributes_to_numbers()
    cv_net = cross_validation(NeuralNetLearner,dataset)
    
    # formatting the output for Learner column
    if dataset.name is 'restaurant':
        formatlearner = ('\tDecisionTreeLearner','\tNeuralNetLearner')
    else:
        formatlearner = ('\t\tDecisionTreeLearner','\t\tNeuralNetLearner')
    
    # formatting the rest of output
    output1 = " ".join([format(x,'.3f') for x in cv_tree[2]])
    print(format(cv_tree[0],'.3f') + '\t' + format(cv_tree[1],'.3f') + '  ' 
          + output1 + '\t' + cv_tree[3] + formatlearner[0])
    output2 = " ".join([format(x,'.3f') for x in cv_net[2]])
    print(format(cv_net[0],'.3f') + '\t' + format(cv_net[1],'.3f') + '  ' 
          + output2 + '\t' + cv_net[3] + formatlearner[1])
    
def main():
    print("Calculating datasets...")
    print("Mean\tStdDev Errors for each fold \t\t\t\t\t\tCorpus\t\tLearner")
    for dataset in ['zoo','iris','orings','restaurant']:
        data = DataSet(name=dataset)
        learn(data)
    
if __name__ == '__main__':
    main()
