from dashboard_app_load import app



def get_feature(feature_type,chart_type):
    
    if feature_type=='NP-TOP_5':

        if chart_type=='NP-CLASS':
            return html.Img(src=app.get_asset_url('np-class-imbalance.png'))
        elif chart_type=='NP-FEATURES':
            return html.Img(src=app.get_asset_url('np-f-import-top5-sm.png'))
        elif chart_type=='NP-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('np-model-scores-title.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('np-xg-cm-raw-up-top5.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('np-xg-cm-norm-up-top5.png'))
        elif chart_type=='NP-ROC':
            return html.Img(src=app.get_asset_url('np-xg-roc-up-top5.png'))
        else:
            return html.Img(src=app.get_asset_url('np-natl-tr.png'))
        
    elif feature_type=='NP-ALL': #2355 features 

        if chart_type=='NP-CLASS':
            return html.Img(src=app.get_asset_url('np-class-imbalance.png'))
        elif chart_type=='NP-FEATURES':
            return html.Img(src=app.get_asset_url('np-f-import-2355-sm.png'))
        elif chart_type=='NP-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('np-model-scores-title.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('np-xg-cm-raw-down-2355.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('np-xg-cm-norm-down-2355.png'))
        elif chart_type=='NP-ROC':
            return html.Img(src=app.get_asset_url('np-xg-roc-down-2355.png'))
        
        else:
            return html.Img(src=app.get_asset_url('np-natl-tr.png'))
    else:
        return html.Img(src=app.get_asset_url('np-natl-tr.png'))
    
     
