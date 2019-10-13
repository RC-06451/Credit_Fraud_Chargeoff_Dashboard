import pandas as pd
import matplotlib.pyplot as plt
import numpy as np    

def plot_feature_importance(classifier,title):
    feature_importance = abs(classifier.coef_[0])
    feature_importance = 100.0 * (feature_importance / feature_importance.max()) #normalize data
    sorted_idx = np.argsort(feature_importance) #sort by value
    pos = np.arange(sorted_idx.shape[0]) + .5
    featfig = plt.figure()
    featax = featfig.add_subplot(1, 1, 1)
    featax.barh(pos, feature_importance[sorted_idx], align='center')
    featax.set_title(title)
    featax.set_yticks(pos)
    featax.set_yticklabels(np.array(X.columns)[sorted_idx], fontsize=8)
    featax.set_xlabel('Relative Feature Importance')
    plt.tight_layout()   
    plt.show()
