



def get_data_feature(feature_type,chart_type):
    
    if feature_type=='NP-TOP_5':

        if chart_type=='NP-CLASS':
            return 'np-class-imbalance.png'
        elif chart_type=='NP-FEATURES':
            return 'np-f-import-top5-sm.png'
        elif chart_type=='NP-MODEL_SCORES':
            return 'np-model-scores-title.png'
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return 'np-xg-cm-raw-up-top5.png'
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return 'np-xg-cm-norm-up-top5.png'
        elif chart_type=='NP-ROC':
            return 'np-xg-roc-up-top5.png'
        else:
            return 'np-natl-tr.png' #default graph
        
    elif feature_type=='NP-ALL': #2355 features 

        if chart_type=='NP-CLASS':
            return 'np-class-imbalance.png'
        elif chart_type=='NP-FEATURES':
            return 'np-f-import-2355-sm.png'
        elif chart_type=='NP-MODEL_SCORES':
            return 'np-model-scores-title.png'
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return 'np-xg-cm-raw-down-2355.png'
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return 'np-xg-cm-norm-down-2355.png'
        elif chart_type=='NP-ROC':
            return 'np-xg-roc-down-2355.png'
        
        else:
            return 'np-natl-tr.png' #default graph
    
    
    elif feature_type=='M6-TOP_5':
        
        if chart_type=='M6-CLASS':
            return 'm6-class-imbalance.png'
        elif chart_type=='M6-FEATURES':
            return 'm6-f-import-top5-sm.png'
        elif chart_type=='M6-MODEL_SCORES':
            return 'm6-model-scores-title.png'
        elif chart_type=='M6-CONFUSION_MATRIX_RAW':
            return 'm6-xg-cm-raw-up-top5.png'
        elif chart_type=='M6-CONFUSION_MATRIX_NORM':
            return 'm6-xg-cm-norm-up-top5.png'
        elif chart_type=='M6-ROC':
            return 'm6-xg-roc-norm-up-top5.png'
        else:
            return 'm6-natl-tr.png' #default graph

        
    elif feature_type=='M6-ALL': #2355 features 

        if chart_type=='M6-CLASS':
            return 'm6-class-imbalance.png'
        elif chart_type=='M6-FEATURES':
            return 'm6-f-import-2355-sm.png'
        elif chart_type=='M6-MODEL_SCORES':
            return 'm6-model-scores-title.png'
        elif chart_type=='M6-CONFUSION_MATRIX_RAW':
            return 'm6-xg-cm-raw-down-2355.png'
        elif chart_type=='M6-CONFUSION_MATRIX_NORM':
            return 'm6-xg-cm-norm-down-2355.png'
        elif chart_type=='M6-ROC':
            return 'm6-roc-down-2355.png'
        else:
            return 'm6-natl-tr.png'  #default graph


    
