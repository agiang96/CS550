'''
file: std_cv.py
author: Alexander Giang
'''
from statistics import (stdev, mean)
from ml_lib.learning import (err_ratio, train_and_test)


def cross_validation(learner, dataset, k=10):
    """Perform k-fold cross_validation
    Run k trials where each trial has a different (k-1)/k percentage
    of the data as training data and 1/k as test data.
    
    Returns tuple (mean_err, std_err, fold_errors, models)
    """
    if k is None:
        k = len(dataset.examples)

    fold_errT = 0   # fold error on training data
    fold_errV = 0   # fold error on validation data
    fold_err_list = [] # holds all the fold error rates
    train_list = [] # holds all the trained data
        
    n = len(dataset.examples)
    examples = dataset.examples
    
    for fold in range(k):   # for each fold
        # Split into train and test
        # Note that this is not a canonical cross validation where
        # every pieces of data is used for training and testing
        # due to the shuffling above.
        train_data, val_data = train_and_test(dataset, fold * (n / k),
                                              (fold + 1) * (n / k))
        train_list.append(train_data)
        
        dataset.examples = train_data
        h = learner(dataset)
        
        # predict and accumulate the error rate on 
        # the training and validation data
        fold_ratio_errT = err_ratio(h,dataset,train_data)
        fold_errT += fold_ratio_errT # accumulating
        fold_ratio_errV = err_ratio(h,dataset,val_data)
        fold_errV += err_ratio(h, dataset, val_data)
        fold_err_list.append(fold_ratio_errV) 
        # Reverting back to original once test is completed
        dataset.examples = examples
        
    # Return average per fold rates
    mean_folds = mean(fold_err_list)
    stdev_folds = stdev(fold_err_list,mean_folds)
    
    # Return values are the mean error rate, the standard deviation of 
    # the error rate, a list containing the error rate for each fold, 
    # and a list of models trained.
    return (mean_folds,stdev_folds,fold_err_list, dataset.name)