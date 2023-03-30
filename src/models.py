################################
### Models to train and test ###
################################

import numpy as np
import torch

### Gravity
def gravity_London(alpha, beta, gamma, G, pop_London, pop, distances):
    return (G.log()+alpha*pop_London.log()+beta*pop.log()-gamma*distances.log()).exp()

def gravity_modified(beta, gamma, Ti, pop, distances, names_cv):
    M = len(pop)
    idx = np.array([i for i in range(M) if i not in names_cv])
    Zi = (pop**beta/distances**gamma).sum()
    Tij = Ti*pop[idx]**beta/(Zi*distances[idx]**gamma)
    return Tij

### Radial
def radial_London(Ti, pop_London, pop, S):
    M = pop.sum()+pop_London
    C = pop_London*Ti/(1-pop_London/M)
    return C*pop/((pop+S)*(pop_London+pop+S))

def p_adhesion(alpha, n, pop, pop_London, S):
    x = (n*pop_London+n*pop+n*S)**alpha
    y = (n*pop_London+n*S)**alpha
    num = (x-y)*((n*pop_London)**alpha+1)
    den = (y+1)*(x+1)
    return num/den

def radial_modified(Ti, alpha, n, pop, pop_London, S, names_cv):
    M = len(pop)
    idx = np.array([i for i in range(M) if i not in names_cv])
    P = p_adhesion(alpha, n, pop, pop_London, S)
    Pi = P.sum()
    return Ti*P[idx]/Pi

### Retail

## Without Ti
def retail1(alphas, beta, gamma,
                pop_London, times_London, nums, names_cv):

    M = len(times_London)
    idx_19 = np.array([i for i in range(M) if i not in names_cv])
    idx_20 = np.array([i for i in range(M, 2*M) if i not in names_cv])-M

    model_19 = torch.Tensor()
    if len(idx_19)>0:
        exponent_19 = -beta*times_London#[idx_19]
        for (idx, alpha) in enumerate(alphas):
            exponent_19 += alpha*torch.Tensor(nums[idx].fillna(0 if alpha==0 else np.nan).loc[10,:].values)
        #names[idx_19]
        Z_19 = exponent_19.exp().sum()
        model_19 = gamma*pop_London*exponent_19[idx_19].exp()/Z_19

    model_20 = torch.Tensor()
    if len(idx_20)>0:
        exponent_20 = -beta*times_London#[idx_20]
        for (idx, alpha) in enumerate(alphas):
            exponent_20 += alpha*torch.Tensor(nums[idx].fillna(0).loc[11,:].values)
        Z_20 = exponent_20.exp().sum()
        #print(len(gamma), pop_London.shape, exponent_20.shape, model_20.shape)
        model_20 = gamma*pop_London*exponent_20[idx_20].exp()/Z_20
    #print(Z_19, Z_20)
    model = torch.cat((model_19, model_20))
    return model

## With Ti
def retail2(alphas, beta,
               Tis, pop_London, times_London, nums, names_cv):

    M = len(times_London)
    idx_19 = np.array([i for i in range(M) if i not in names_cv])
    idx_20 = np.array([i for i in range(M, 2*M) if i not in names_cv])-M

    model_19 = torch.Tensor()
    if len(idx_19)>0:
        exponent_19 = -beta*times_London#[idx_19]
        for (idx, alpha) in enumerate(alphas):
            exponent_19 += alpha*torch.Tensor(nums[idx].fillna(0).loc[10,:].values)
        #names[idx_19]
        Z_19 = exponent_19.exp().sum()
        model_19 = Tis[0]*exponent_19[idx_19].exp()/Z_19

    model_20 = torch.Tensor()
    if len(idx_20)>0:
        exponent_20 = -beta*times_London#[idx_20]
        for (idx, alpha) in enumerate(alphas):
            exponent_20 += alpha*torch.Tensor(nums[idx].fillna(0).loc[11,:].values)
        Z_20 = exponent_20.exp().sum()
        #print(len(gamma), pop_London.shape, exponent_20.shape, model_20.shape)
        model_20 = Tis[1]*exponent_20[idx_20].exp()/Z_20
    #print(Z_19, Z_20)
    model = torch.cat((model_19, model_20))
    return model
