import pickle
import os
dirpath=os.getcwd()
dirpath=dirpath+"/content_load"

#load trained XGBoost models
pickle_in1 = open(dirpath+"/np-xgboost-down-top5-new.pickle","rb")
np_clf_top5 = pickle.load(pickle_in1)

pickle_in2 = open(dirpath+"/np-xgboost-down-2355-new.pickle","rb")
np_clf_2355 = pickle.load(pickle_in2)

pickle_in3 = open(dirpath+"/m6-xgboost-down-top5-new.pickle","rb")
m6_clf_top5 = pickle.load(pickle_in3)

pickle_in4 = open(dirpath+"/m6-xgboost-down-2355-new.pickle","rb")
m6_clf_2355 = pickle.load(pickle_in4)
