
#load trained xgboost pickle files
from pickle.xg_pickle_load import np_clf_top5,np_clf_2355,m6_clf_top5,m6_clf_2355

#load simulated customer datasets for both Nonpayer (NP) and Month Six Deliquent (M6) groups
from sim_data.sim_customer_df_load import df_np,df_m6,df_np_top5,df_np_2355,df_m6_top5,df_m6_2355


#predict simulated data
X_name=df_np.iloc[:,1]

#np-top5
X_test=df_np_top5
X_test=X_test.values

y_pred_np_top5=np_clf_top5.predict(X_test)
y_pred_proba_np_top5=np_clf_top5.predict_proba(X_test)

#np-2355
X_test=df_np_2355
X_test=X_test.values

y_pred_np_2355=np_clf_2355.predict(X_test)
y_pred_proba_np_2355=np_clf_2355.predict_proba(X_test)

#m6-top5
X_test=df_m6_top5
X_test=X_test.values

y_pred_m6_top5=m6_clf_top5.predict(X_test)
y_pred_proba_m6_top5=m6_clf_top5.predict_proba(X_test)

#m6-2355
X_test=df_m6_2355
X_test=X_test.values

y_pred_m6_2355=m6_clf_2355.predict(X_test)
y_pred_proba_m6_2355=m6_clf_2355.predict_proba(X_test)

