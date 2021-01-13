#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

#provide log of Vce and Sigmae
def Dist_indicator(Sigmae, Vce, AMmodel, Cmodel):
    n_gal = len(Sigmae)
    binM = 36
    bins = np.linspace(9., 12.5, binM)
    grid = pd.read_csv('GridModels.csv')

    v_int = np.zeros((n_gal, binM))
    for ij in range(binM):
        v_int[:, ij] = np.interp(
            Sigmae, grid['Sigmae_M' + np.str(bins[ij])].values,
            grid[AMmodel + '_Vce_M' + np.str(bins[ij]) +'_'+ Cmodel].values)

    m_pred = np.zeros(n_gal)
    for pp in range(n_gal):
        m_pred[pp] = np.interp(Vce[pp], v_int[pp, :], bins)

    return(m_pred)

