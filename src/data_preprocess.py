###########################
### Data pre-processing ###
###########################

import pandas as pd
import numpy as np
import torch

from raw_data import names_sij

### Import data
path = 'BritishDrugDynamics/data/'

pop_police = pd.read_csv(path+'demographic/population_policeforces.csv')
times = pd.read_csv(path+'gmaps/times_min_police.csv', index_col='name')

workforce_100k = pd.read_csv(path+'police_data/workforce/local_resolution/workforce_mean_100k.csv')
knifecrime_100k = pd.read_csv(path+'police_data/knifecrime/local_resolution/knifecrime_100k.csv')

deaths_misuse_polices_100k = pd.read_csv('deaths_drugs_alt/misuse_polices_100k.csv')
deaths_poisoning_polices_100k = pd.read_csv('deaths_drugs_alt/poisoning_polices_100k.csv')

admissions_misuse_polices_100k = pd.read_csv(path+'drugs_usage/hospital_admissions/local_resolution/misuse_polices_100k.csv')
admissions_primary_polices_100k = pd.read_csv(path+'drugs_usage/hospital_admissions/local_resolution/primary_polices_100k.csv')

gdhi = pd.read_csv('gdhi_police.csv', index_col='index')

data = pd.read_csv('data_countylines_metropolitan.csv', index_col='name')
data = data.drop(columns=['ranking model 2018'], index=['Metropolitan Police', 'City of London'])
data = data.sort_index()

### Pre-process data
polices = workforce_100k.columns[1:-2].to_list()
sorted_polices = np.sort(polices.copy())
polices_London = [p for p in polices if p != 'Metropolitan Police' and p != 'City of London']

times_London = times.loc['Metropolitan Police', :].to_frame('cij')

pop_2019 = pop_police[polices].T[10].to_frame('Pi')
pop_London = int(pop_2019.loc[['Metropolitan Police', 'City of London'],:].sum())

names = data.index


### arrays
log_deaths = deaths_misuse_polices_100k[polices].copy()
log_misuse = admissions_misuse_polices_100k[polices].copy()
log_primary = admissions_primary_polices_100k[polices].copy()
log_workforce = workforce_100k[polices].copy()
log_knifecrime = knifecrime_100k[polices].copy()

log_gdhi = gdhi.T.reset_index(drop=True)
log_gdhi = pd.concat([log_gdhi, log_gdhi]).set_index(pd.Index([10, 11]))

log_deaths = np.log(log_deaths.replace(0, 1))
log_misuse = np.log(log_misuse.replace(0, 1))
log_primary = np.log(log_primary.replace(0, 1))
log_workforce = np.log(log_workforce.replace(0, 1))
log_knifecrime = np.log(log_knifecrime.replace(0, 1))
log_gdhi = np.log(log_gdhi.replace(0, 1))

### distances London polices
d_Lj = [186.68, 54.16,  97.18, 303.45, 411.72, 492.79, 205.01, 344.22, 168.97, 431.52, 59.18, 178.47, 319.08,
        125.77, 49.39, 301.74, 92.12, 353.04, 163.20, 228.51, 338.32, 185.36, 335.01, 109.23, 453.45, 200.47,
        258.69, 254.22, 126.10, 48.57, 86.10, 91.58, 156.59, 234.11, 190.17, 325.40, 127.04, 293.11, 218.71, 
        360.05, 297.20]
d_Lj = torch.Tensor(d_Lj)


### Populations for radial model
S_ij = torch.zeros(len(names))
for i in range(len(names)):
    for name in names_sij[i]:
        if name not in names:
            print(i, name)

for i in range(len(names)):
    #print(names_sij[i])
    S_ij[i] = pop_2019.loc[names_sij[i], :].sum().values[0]