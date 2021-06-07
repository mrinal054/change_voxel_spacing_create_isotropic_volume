## Change voxel spacing / Create isotropic volume
This code changes voxel spacing of a 3D volume. It can also be used to generate isotropic volume.

In deep learning, to train 3D data, often it is preferred to have all data with same voxel spacing. But the original 3D images may not have the same voxel spacing. This code can be used to change voxel spacing of a 3D image. It can also be used to generate isotropic volumes. Training with isotropic 3D volume is very common in deep learning.

### Description of `change_voxel_spacing` function
* Function `change_voxel_spacing` changes voxel spacing

* Input parameters: <br>
    `D`: Original data <br>
    `org_spacing`: Original voxel spacing <br>
    `new_spacing`: New voxel spacing defined by the user
    
* Output:
    Returns volume with new spacing in `int16` format

#### Requirements
* `numpy`
* `pydicom`
* `scipy`
