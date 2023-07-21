import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
import pickle
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.metrics import roc_curve, auc, roc_auc_score
import matplotlib
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
from yellowbrick.classifier import ROCAUC
from yellowbrick.datasets import load_game
#
#%matplotlib inline
matplotlib.rcParams.update({'font.size': 20})


#df_data = pd.read_csv('final_dataset.csv')
list_of_train = [1,2,3,4]
list_of_test  = [1,2,3,4]
df_train_all = pd.DataFrame()
df_test_all  = pd.DataFrame()
df_all  = pd.read_csv('final_dataset.csv')

def compute_roc_auc_train(scaled_train_data_x, train_data_y):
    y_predict = rfc.predict_proba(scaled_train_data_x)[:,1]
    fpr, tpr, thresholds = roc_curve(train_data_y, y_predict)
    auc_score = auc(fpr, tpr)
    return fpr, tpr, auc_score

def compute_roc_auc_test(scaled_test_data_x, test_data_y):
    y_predict = rfc.predict_proba(scaled_test_data_x)[:,1]
    fpr, tpr, thresholds = roc_curve(test_data_y, y_predict)
    auc_score = auc(fpr, tpr)
    return fpr, tpr, auc_score




train_data_x = df_all.iloc[:, 3:-2]
train_data_y = df_all.iloc[:, -1:]

print(train_data_x)
#print(train_data_x.shape)

X = pd.DataFrame(train_data_x)
y = pd.DataFrame(train_data_y)
#exit()
#test_data_x = df_test_all.iloc[:, :-1]
#test_data_y = df_test_all.iloc[:, -1:]


#Example
#train_data_x = df_train_all.iloc[:4155, :-1]
#train_data_y = df_train_all.iloc[:4155, -1:]

#test_data_x = df_test_all.iloc[:4155, :-1]
#test_data_y = df_test_all.iloc[:4155, -1:]




#exit()

#train_data_y = sc.fit_transform(train_data_y)
#test_data_y  = sc.fit_transform(test_data_y)


#print(train_data_y.values.ravel())
#rfc = RandomForestClassifier(n_estimators=200, max_depth=16, max_features=100)
#rfc = RandomForestClassifier(n_estimators=200, class_weight='balanced')

#dict_weights = {0:16.10, 1:0.51}

rfc = DecisionTreeClassifier(max_features=200)
parameters = {
    "n_estimators":[200, 200, 200, 200, 200],
    "max_features":[100, 200, 300, 400, 500]
}


fprs, tprs, scores = [], [], []

cv = StratifiedKFold(n_splits=4, random_state=42, shuffle=True)

#cv = KFold(n_splits=4, random_state=42, shuffle=True)



print(X.shape)
print(y.shape)

for (train, test), i in zip(cv.split(X, y), range(4)):
    # print(X.iloc[train])
    # print(X.iloc[test])
    # print(X.iloc[train].shape)
    # print(X.iloc[test].shape)
    # exit()
    sc = StandardScaler()
    # sc = Normalizer()
    scaled_train_data_x = sc.fit_transform(X.iloc[train])
    scaled_test_data_x = sc.transform(X.iloc[test])
    #scaled_train_data_x = pd.DataFrame(scaled_train_data_x)
    #scaled_test_data_x = pd.DataFrame(scaled_test_data_x)

    train_data_y = y.iloc[train].values.ravel()
    test_data_y = y.iloc[test].values.ravel()

    #print(type(scaled_train_data_x))

    #rfc.fit(scaled_train_data_x, train_data_y)
    visualizer = ROCAUC(rfc, classes=[0, 1, 2, 3, 4])
    visualizer.fit(scaled_train_data_x, train_data_y)  # Fit the training data to the visualizer
    visualizer.score(scaled_test_data_x, test_data_y)  # Evaluate the model on the test data
    visualizer.show()
    #_, _, auc_score_train = compute_roc_auc_train(scaled_train_data_x, train_data_y)
    #fpr, tpr, auc_score = compute_roc_auc_test(scaled_test_data_x, test_data_y)
    #scores.append((auc_score_train, auc_score))
    #fprs.append(fpr)
    #tprs.append(tpr)
    #scaled_test_data_x = X.iloc[test]
    #test_data_y = y.iloc[test].values.ravel()

    y_pred = rfc.predict(scaled_test_data_x)
    accuracy = metrics.accuracy_score(y_pred, test_data_y)
    print(accuracy)
    print(confusion_matrix(test_data_y, y_pred))
    print(classification_report(test_data_y, y_pred))
    print(accuracy_score(test_data_y, y_pred))

    #precision = precision_score(test_data_y, y_pred)



    precision = precision_score(test_data_y, y_pred, average='micro')
    print('Precision: %.3f', precision)
    #recall = recall_score(test_data_y, y_pred)
    recall = recall_score(test_data_y, y_pred, average='micro')
    print('Recall: %.3f', recall)
    #score = f1_score(test_data_y, y_pred)
    score = f1_score(test_data_y, y_pred, average='micro')
    print('F-Measure: %.3f', score)



def plot_roc_curve_simple(fprs, tprs):
    plt.figure(figsize=(8,8))
    for i in range(len(fprs)):
        roc_auc = auc(fprs[i], tprs[i])
        ysmoothed = gaussian_filter1d(tprs[i], sigma=2)
        plt.plot(fprs[i], tprs[i], label='ROC fold %d (AUC = %0.2f)' % (i+1, roc_auc))
        i +=1
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve for Random Forest')
    plt.legend(loc='best')
    #plt.savefig('Authentication_Bypass_RF_yes_shuffle.png')
    plt.show()




#plot_roc_curve_simple(fprs, tprs);
#pd.DataFrame(scores, columns=['AUC Train', 'AUC Test'])




# #Below The 4fold
# #rfc.fit(scaled_train_data_x, train_data_y.values.ravel())
# #rfc.fit(scaled_train_data_x, train_data_y)
# y_pred = rfc.predict(scaled_test_data_x)
# print(y_pred)
# print(y_pred.shape)
# accuracy = metrics.accuracy_score(y_pred, test_data_y)
#
# #apple
# #---------------Metrics------------
#
# print(accuracy)
# print(confusion_matrix(test_data_y,y_pred))
# print(classification_report(test_data_y,y_pred))
# print(accuracy_score(test_data_y, y_pred))
#
#
# precision = precision_score(test_data_y, y_pred)
# print('Precision: %.3f', precision)
# recall = recall_score(test_data_y, y_pred)
# print('Recall: %.3f', recall)
# score = f1_score(test_data_y, y_pred)
# print('F-Measure: %.3f', score)
