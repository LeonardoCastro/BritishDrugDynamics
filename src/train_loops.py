######################
### Training loops ###
######################

import numpy as np
import torch
from torch import nn

from functions import cost_gauss, cost_poisson
from models import gravity_modified, radial_modified, retail1, retail2

def train_loop_gravity(target, pop, distances, Tis,
                    wd, distribution, names_cv,
                    iterations=1000, lr=0.0000001, print_=False,
                    beta=1, gamma=2):

    beta = nn.Parameter(torch.Tensor([beta]))
    gamma = nn.Parameter(torch.Tensor([gamma]))

    n_params = 2
    optimizer = torch.optim.SGD([beta, gamma], lr=lr, weight_decay=wd)
    losses = torch.zeros(iterations)
    params = torch.zeros((n_params, iterations))

    names_cv_19 = [i for i in names_cv if i < len(pop)]
    names_cv_20 = [i - len(pop) for i in names_cv if i not in names_cv_19]

    for step in range(iterations):

        #compute prediction
        prediction_19 = gravity_modified(beta, gamma, Tis[0], pop, distances, names_cv_19)
        prediction_20 = gravity_modified(beta, gamma, Tis[1], pop, distances, names_cv_20)
        prediction = torch.cat([prediction_19, prediction_20])

        if distribution == 'Poisson':
            loss = cost_poisson(target, prediction)
        elif distribution == 'Gauss':
            loss = cost_gauss(target, prediction)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step%1000==0:
            loss = loss.item()
            if print_:
                print(f"loss: {loss:>4f} [{step:>3d}]")

        losses[step] = loss
        params[:, step] = torch.Tensor([beta, gamma])
    return np.array(params.detach()), np.array(losses.detach())


def train_loop_radial(target, pop, pop_London, Tis, S,
                         wd, distribution, names_cv,
                       iterations=1000, lr=0.0000001, print_=False,
                       alpha=1, n=1):

    n = nn.Parameter(torch.Tensor([n]))
    alpha = nn.Parameter(torch.Tensor([alpha]))

    n_params = 2
    optimizer = torch.optim.SGD([n, alpha], lr=lr, weight_decay=wd)
    losses = torch.zeros(iterations)
    params = torch.zeros((n_params, iterations))

    names_cv_19 = [i for i in names_cv if i < len(pop)]
    names_cv_20 = [i - len(pop) for i in names_cv if i not in names_cv_19]

    for step in range(iterations):

        #compute prediction
        prediction_19 = radial_modified(Tis[0], alpha, n, pop, pop_London, S, names_cv_19)
        prediction_20 = radial_modified(Tis[1], alpha, n, pop, pop_London, S, names_cv_20)
        prediction = torch.cat([prediction_19, prediction_20])

        if distribution == 'Poisson':
            loss = cost_poisson(target, prediction)
        elif distribution == 'Gauss':
            loss = cost_gauss(target, prediction)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step%1000==0:
            loss = loss.item()
            if print_:
                print(f"loss: {loss:>4f} [{step:>3d}]")

        losses[step] = loss
        params[:, step] = torch.Tensor([alpha, n])

    return np.array(params.detach()), np.array(losses.detach())


def train_loop_retail1(target, nums, pop, times,
               names_cv, combination, distribution, 
               tuple_gamma=(1e-3,1), iterations=1000, lr=0.0000001, wd=1,
               alpha1=0.1, alpha2=0.1, alpha3=0.1, alpha4=0.1,
               beta=0.1, gamma=0.1, print_=False):

    alpha1 = nn.Parameter(torch.Tensor([alpha1]))
    alpha2 = nn.Parameter(torch.Tensor([alpha2]))
    alpha3 = nn.Parameter(torch.Tensor([alpha3]))
    alpha4 = nn.Parameter(torch.Tensor([alpha4]))
    beta = nn.Parameter(torch.Tensor([beta]))
    gamma = nn.Parameter(torch.Tensor([gamma]))

    optimizer = torch.optim.SGD([alpha1, alpha2, alpha3, alpha4, beta, gamma],
                                lr=lr, weight_decay=wd)
    n_params = 6
    losses = torch.zeros(iterations)
    params = torch.zeros((n_params, iterations))
    for step in range(iterations):
        alphas = [alpha1, alpha2, alpha3, alpha4]

        #compute prediction
        prediction = retail1(alpha1, alpha2, alpha3, alpha4,
                                 beta, gamma,
                                 pop, times, nums, names_cv)

        if distribution == 'Poisson':
            loss = cost_poisson(target, prediction)
        elif distribution == 'Gauss':
            loss = cost_gauss(target, prediction)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            for (i, coeff) in enumerate(combination):
                if coeff==0:
                    alphas[i].clamp_(0,0)
                #else:
                #    alphas[i].clamp_(-n, n)
            beta.clamp_(min=0)
            gamma.clamp_(min=0)

        if step%1000==0:
            loss = loss.item()
            if print_:
                print(f"loss: {loss:>4f} [{step:>3d}]")

        losses[step] = loss
        params[:, step] = torch.Tensor([alpha1, alpha2, alpha3, alpha4, beta, gamma])

    return np.array(params.detach()),  np.array(losses.detach())

def train_loop_retail2(target, nums, Tis, pop, times,
                names_cv, combination, distribution, params_init,
                iterations=1000, lr=0.0000001, wd=1,
                print_=False):

    parameters = []
    for param in params_init:
        parameters.append(nn.Parameter(torch.Tensor([param])))

    optimizer = torch.optim.SGD(parameters, lr=lr, weight_decay=wd)

    n_params = len(parameters)
    losses = torch.zeros(iterations)
    params = torch.zeros((n_params, iterations))
    for step in range(iterations):
        alphas = parameters[:-1]
        beta = parameters[-1]

        #compute prediction
        prediction = retail2(alphas, beta,
                             Tis, pop, times, nums, names_cv)

        if distribution == 'Poisson':
            loss = cost_poisson(target, prediction)
        elif distribution == 'Gauss':
            loss = cost_gauss(target, prediction)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            for (i, coeff) in enumerate(combination):
                if coeff==0:
                    alphas[i].clamp_(0,0)
                #else:
                #    alphas[i].clamp_(-n, n)
            beta.clamp_(min=0)

        if step%1000==0:
            loss = loss.item()
            if print_:
                print(f"loss: {loss:>4f} [{step:>3d}]")

        losses[step] = loss
        params[:, step] = torch.Tensor(parameters)
    return np.array(params.detach()), np.array(losses.detach())
