# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:26:59 2019
import numpy as 
@author: admin
"""

import numpy as np

def perceptron_single_step_update(
        feature_vector,
        label,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the perceptron algorithm.

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        current_theta - The current theta being used by the perceptron
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the perceptron
            algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    # Your code here
    
    if label*(np.dot(feature_vector , current_theta) + current_theta_0 ) <= .009 :
        current_theta =  current_theta + np.multiply( label , feature_vector) 
        current_theta_0 = current_theta_0 + label
        tup = ( current_theta , current_theta_0)
    else:
        tup = ( current_theta , current_theta_0)
    return tup    
  
   
    


feature_matrix = np.array( [[-0.08178806, -0.32043124, -0.11831542],
 [-0.40283178,  0.35375058, -0.18152935],
 [ 0.25772617,  0.15779362 ,-0.18555544],
 [-0.3385156 ,  0.18669764 , 0.22939441],
 [ 0.49304159 , 0.18148859 , 0.4719957 ]])
labels = np.array([-1 , 1, -1, -1,  1])
T = 1
ncol = feature_matrix.shape[1] # no of coloumns in the feature matrix
current_theta = np.zeros(ncol,)
sum1 = np.empty((1, ncol))
sum2 = 0
n = feature_matrix.shape[0] #no of rows in the feature matrix
current_theta_0 = 0
tup = (current_theta, current_theta_0)
for t in range(T):
        #for i in get_order(feature_matrix.shape[0]):
            # Your code here
        for i in range(n):
                feature_vector = feature_matrix[i]
   
                label = labels[i]
                current_theta = tup[0]
                current_theta_0 = tup[1]
                tup = perceptron_single_step_update(feature_vector, label, current_theta, current_theta_0)
                sum1 = np.add( sum1, current_theta)              
                sum2 = sum2 + current_theta_0
sum11 = sum1/(n*T)
sum22 = sum2/(n*T)
sum11 = sum11[0]
c = (sum11, sum22)
print(c)