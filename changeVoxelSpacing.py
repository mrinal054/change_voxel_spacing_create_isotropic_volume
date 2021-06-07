# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:41:31 2021

@author: mrinal

* This code changes voxel spacing

* Input parameters:
    D -> Original data
    org_spacing -> Original voxel spacing
    new_spacing -> New voxel spacing
    
* Output:
    Returns volume with new spacing in int16 format

"""
import numpy as np
from scipy.interpolate import RegularGridInterpolator

def change_voxel_spacing(D, org_spacing, new_spacing):
    # Get new volume size
    D = np.squeeze(D)
    sz_org = D.shape
    ratio = org_spacing/new_spacing
    sz_new = np.ceil((D.shape-np.array([1]))*ratio)+np.array([1])
    sz_new = sz_new.astype('int16')

    # Generate voxel locations for the original data
    Xa = np.arange(0, sz_org[0], 1)*org_spacing[0] 
    Ya = np.arange(0, sz_org[1], 1)*org_spacing[1]
    Za = np.arange(0, sz_org[2], 1)*org_spacing[2]
    
    # Generate voxel locations for the new data
    Xb, Yb, Zb = np.meshgrid(np.arange(0, sz_new[0], 1)*new_spacing[0],
                             np.arange(0, sz_new[1], 1)*new_spacing[1],
                             np.arange(0, sz_new[2], 1)*new_spacing[2])
    
    # Do interpolation
    fn = RegularGridInterpolator((Ya,Xa,Za), D, bounds_error=False)
    
    Xb_f, Yb_f, Zb_f = Xb.flatten(), Yb.flatten(), Zb.flatten() #flatten data

    interpPoints = np.array([Yb_f, Xb_f,  Zb_f]) 
    
    D_new = fn(interpPoints.T)
    D_new = np.reshape(D_new, Xb.shape)
    D_new = D_new.astype('int16') #saving in int16 format    
    
    return D_new


            