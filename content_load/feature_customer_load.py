




#load trained xgboost pickle files
from .xg_pickle_load import np_clf_top5,np_clf_2355,m6_clf_top5,m6_clf_2355



#load simulated customer datasets for both Nonpayer (NP) and Month Six Deliquent (M6) groups
from .sim_customer_df_load import df_np,df_m6,df_np_top5,df_np_2355,df_m6_top5,df_m6_2355


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


#get customer information
def get_customer_feature(feature_type,chart_type):
    if feature_type=='NP-TOP_5':

        if chart_type=='NP-CUST':
            
            text_risk="*****CUSTOMERS AT-RISK FOR NON-PAYER GROUP*****\n\n"
            text_risk=text_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_risk=text_risk+"--------------------------------------------------------------------\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR NON-PAYER GROUP*****\n\n"
            text_no_risk=text_no_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_no_risk=text_no_risk+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                if y_pred_np_top5[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_np_top5[index-1,1]).rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_np_top5[index-1,1]).rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        
        elif chart_type=='NP-LIST':
            text=""
            text=text+"Customer Number"+"\t"+"Customer Name"+"\n"
            text=text+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
       
        else:
            return 'This will hold Nonpayer (NP) customer information'
        
    elif feature_type=='NP-ALL': #2355 features

        if chart_type=='NP-CUST':
            text_risk="*****CUSTOMERS AT-RISK FOR NON-PAYER GROUP*****\n\n"
            text_risk=text_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_risk=text_risk+"--------------------------------------------------------------------\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR NON-PAYER GROUP*****\n\n"
            text_no_risk=text_no_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_no_risk=text_no_risk+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                if y_pred_np_2355[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_np_2355[index-1,1]).rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_np_2355[index-1,1]).rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        
        elif chart_type=='NP-LIST':
            text=""
            text=text+"Customer Number"+"\t"+"Customer Name"+"\n"
            text=text+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
        
        else:
            return 'This will hold Nonpayer (NP) customer information'


    elif feature_type=='M6-TOP_5':
        
        if chart_type=='M6-CUST':
            text_risk="*****CUSTOMERS AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            text_risk=text_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_risk=text_risk+"--------------------------------------------------------------------\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            text_no_risk=text_no_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_no_risk=text_no_risk+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                if y_pred_m6_top5[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_m6_top5[index-1,1]).rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_m6_top5[index-1,1]).rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        elif chart_type=='M6-LIST':
            text=""
            text=text+"Customer Number"+"\t"+"Customer Name"+"\n"
            text=text+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
            
        else:
            return 'This will hold Month Six Delinquent (M6) customer information'

        
    else: #2355 features 

        if chart_type=='M6-CUST':
            text_risk="*****CUSTOMERS AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            text_risk=text_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_risk=text_risk+"--------------------------------------------------------------------\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            text_no_risk=text_no_risk+"Customer Number"+"\t"+"Customer Name"+"\t"+"Probability"+"\n"
            text_no_risk=text_no_risk+"--------------------------------------------------------------------\n"
            
            for index in range(1,21):
                if y_pred_m6_2355[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_m6_2355[index-1,1]).rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(y_pred_proba_m6_2355[index-1,1]).rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        
        elif chart_type=='M6-LIST':
            text=""
            text=text+"Customer Number"+"\t"+"Customer Name"+"\n"
            text=text+"--------------------------------------------------------------------\n"
          
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
        
        else:
            return 'This will hold Month Six Delinquent (M6) customer information'
    



    

    
