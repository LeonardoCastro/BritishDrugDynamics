########################
### Support function ###
########################

import numpy as np
import torch
import math

### Coeffs
def coeffs(n_array):
    coeff_list = []
    ITER_MAX = 100
    
    for ones in range(0, n_array+1):
        coeffs_ = []
        perm_ = np.zeros(n_array)
        perm_[:ones] = 1
        
        iter_ = 0
        while len(coeffs_) != math.comb(n_array, ones) and iter_ < ITER_MAX:
            p = np.random.permutation(perm_)
            bools_ = [np.array_equal(p, arr) for arr in coeffs_]
            if sum(bools_) == 0:
                coeffs_.append(p)
            iter_ = iter_ + 1
        coeff_list = coeff_list + coeffs_
    return coeff_list

### Costs
def cost_gauss(observations, model):
    N = len(observations)
    cost = ((observations-model)**2).sum()/N
    return cost

def cost_poisson(observations, model):
    idx = np.where(model!=0)[0]

    observations = observations[idx]
    model = model[idx]

    N = len(idx)
    cost = (model-observations*model.log()).sum()/N

    return cost

### Likelihoods
def log_poisson(xs, lambdas):
    idx = np.where(xs!=0)[0]
    vec = xs[idx]*lambdas[idx].log()-lambdas[idx]-xs[idx]*xs[idx].log()+xs[idx]
    return vec.sum()

def log_gauss(xs, mus):
    sigma = xs.std()
    vec = -1*(xs-mus)**2/(2*sigma)-(2*math.pi*(sigma**2)).log()/2
    return vec.sum()

### Comparisons
def sorensen(lines_data, lines_model):
    dummy = torch.cat((lines_model.reshape(1, len(lines_model)), lines_data.reshape(1, len(lines_data))))
    min_ = dummy.min(dim=0).values.sum()
    S = 2*min_/(lines_model.sum()+lines_data.sum())
    return S

AIC = lambda k, log_L: 2*k-2*log_L

BIC = lambda k, log_L: 2*np.log(k)-2*log_L

### Cross-validation
def get_permutations(n_sample, n_perm, M):
    perms = set()
    list_perms = list()
    for i in range(n_sample):
        while True:
            perm = np.random.permutation(M)[:n_perm]
            key = tuple(perm)
            if key not in perms:
                perms.update(key)
                list_perms.append(perm)
                break
    return list_perms
