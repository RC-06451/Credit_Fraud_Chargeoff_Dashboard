import pandas as pd

import os
dirpath=os.getcwd()
dirpath=dirpath+"/content_load"

#read in both the simulated non-payer(np) and month six delinquent (m6) customer data
df_np = pd.read_csv(dirpath+'/np-sim-data-num-test.csv')
df_m6 = pd.read_csv(dirpath+'/m6-sim-data-num-test.csv')
df_np_top5 = pd.read_csv(dirpath+'/np-sim-data-top5-out.csv')
df_np_2355 = pd.read_csv(dirpath+'/np-sim-data-2355-out.csv')
df_m6_top5 = pd.read_csv(dirpath+'/m6-sim-data-top5-out.csv')
df_m6_2355 = pd.read_csv(dirpath+'/m6-sim-data-2355-out.csv')
