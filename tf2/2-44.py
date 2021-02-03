import numpy as np
from sklearn.datasets import load_iris
data=load_iris()
iris_target=data.target
iris_data=np.float32(data.data)