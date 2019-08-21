import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

# Index levels

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hierindex = list(zip(outside,inside))
print(pd.MultiIndex.from_tuples(hierindex))

