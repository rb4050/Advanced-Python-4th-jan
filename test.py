# this is python script

import numpy as np

# declaring a list
a = [1,2,3,4,5]
print(a,type(a))

# create a numpy array
b= np.array(a)
print(f"variable b : {b}, Type : {type(b)}")

# check dim and shape of array
print(b.ndim)
print(b.shape)

