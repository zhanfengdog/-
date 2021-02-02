import numpy as np
from matplotlib import pyplot as plt
A=np.array([[5],[4]])
C=np.array([[4],[6]])
B=A.T.dot(C)
AA=np.linalg.inv(A.T.dot(A))
l=AA.dot(B)
p=A.dot(l)
3=np.linspace(-2,2,10)
3.shape=(1,10)
33=A.dot(3)
fig=plt.Figure()

a3=fig.add_subplot(111)
a3.plot(33[0,:],33[1,:])
a3.plot(A[0],A[1],'ko')
a3.plot([C[0],P[0]],[C[1],p[1]],'r-o')








