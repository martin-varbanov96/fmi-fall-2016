import numpy as np


n = 10
dMat = 0.05*np.random.random_integers(1, 100, (n, n))
dMat = np.tril(dMat, -1)+np.tril(dMat, -1).T
# dMat = (dMat + dMat.T)/2
ro = 80.0
piMat = np.zeros((n, n))
for i in range(n):
    rowSum = 0.0
    weightSum = 0.0
    for j in range(n):
        if j != i:
            weightSum += 1.0/dMat[i, j]
    for j in range(n):
        lowerBound = np.ceil(ro*np.exp(-dMat[i, j]))
        upperBound = lowerBound + 100 - ro
        if j != i:
            piMat[i, j] = np.random.random_integers(lowerBound, upperBound) / (100 * dMat[i, j] * weightSum)
            rowSum += piMat[i, j]
    piMat[i, i] = 1.0 - rowSum
evvBin = np.linalg.eig(piMat.T)
print('dMat:\n',dMat, '\npiMat:\n', piMat, '\nEigenvalues:\n', evvBin[0], '\nEigenvectors:\n', evvBin[1].T)
