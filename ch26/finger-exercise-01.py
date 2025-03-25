# Finger exercise: Write code to plot the ROC curve and compute
# the AUROC when the model built in Figure 26-16 is tested on 200
# randomly chosen competitors. Use that code to investigate the
# impact of the number of training examples (try varying it from 10 to
# 1010 in increments of 50) on the AUROC.

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model as sklm
import sklearn.metrics as skm

def sensitivity(true_pos, false_neg):
    try:
        return true_pos / (true_pos + false_neg)
    except ZeroDivisionError:
        return float('nan')
    
def specificity(true_neg, false_pos):
    try:
        return true_neg / (true_neg + false_pos)
    except ZeroDivisionError:
        return float('nan')

class Runner(object):
    def __init__(self, name, gender, age, time):
        self._name = name
        self._feature_vec = np.array([age, time])
        self._label = gender

    def feature_dist(self, other):
        return ((self._feature_vec - other._feature_vec)**2).sum()**0.5
    
    def get_time(self):
        return self._feature_vec[1]
    
    def get_age(self):
        return self._feature_vec[0]
    
    def get_label(self):
        return self._label
    
    def get_features(self):
        return self._feature_vec
    
    def __str__(self):
        return (f'{self._name}: {self.get_age()}, ' +
                f'{self.get_time()}, {self._label}')
    
def build_marathon_examples(file_name):
    df = pd.read_csv(file_name)
    examples = []
    for index, row in df.iterrows():
        a = Runner(row['Name'], row['Gender'], row['Age'], row['Time'])
        examples.append(a)
    return examples

def divide_80_20(examples):
    sample_indices = random.sample(range(len(examples)), len(examples)//5)
    training_set, test_set = [], []
    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set

def apply_model(model, test_set, label, prob=0.5):
    # Create vector containing feature vectors for all test examples
    test_feature_vecs = [e.get_features() for e in test_set]
    probs = model.predict_proba(test_feature_vecs)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if test_set[i].get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if test_set[i].get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg

def build_ROC(model, test_set, label, title, plot=True):
    xVals, yVals = [], []
    for p in np.arange(0, 1, 0.01):
        true_pos, false_pos, true_neg, false_neg = apply_model(
            model, test_set, label, p)
        xVals.append(1.0 - specificity(true_neg, false_pos))
        yVals.append(sensitivity(true_pos, false_neg))
    auroc = skm.auc(xVals, yVals)
    if plot:
        plt.plot(xVals, yVals)
        plt.plot([0,1], [0,1,], '--')
        plt.title(title + ' (AUROC = ' + str(round(auroc, 3)) + ')')
        plt.xlabel('1-Specificity')
        plt.ylabel('Sensitivity')
    return auroc

# plot the ROC curve and compute the AUROC when the model built in
# Figure 26-16 is tested on 200 randomly chosen competitors
random.seed(0)
examples = build_marathon_examples('ch26/bm_results2012.csv')
training_set, test_set = divide_80_20(examples)
test_set = random.sample(test_set, 200)
feature_vecs, labels = [], []
for e in training_set:
    feature_vecs.append([e.get_age(), e.get_time()])
    labels.append(e.get_label())
model = sklm.LogisticRegression().fit(feature_vecs, labels)
true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, 'M', 0.5)
build_ROC(model, test_set, 'M', 'ROC for Predicting Gender')

# investigate the impact of the number of training examples (try varying it from 10 to
# 1010 in increments of 50) on the AUROC.
for i in range(10, 1010+1, 50):
    reduced_training_set = random.sample(training_set, i)
    feature_vecs, labels = [], []
    for e in reduced_training_set:
        feature_vecs.append([e.get_age(), e.get_time()])
        labels.append(e.get_label())
    model = sklm.LogisticRegression().fit(feature_vecs, labels)
    true_pos, false_pos, true_neg, false_neg = apply_model(model, test_set, 'M', 0.5)
    auroc = build_ROC(model, test_set, 'M', 'ROC for Predicting Gender', plot=False)
    print(f'Training set = {len(reduced_training_set)}, AUROC = {round(auroc, 3)}')