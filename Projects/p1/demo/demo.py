import problem49a as chole
import problem49b as levin
import numpy as np
print("*********Cholesky Part*********")
print("Matrix A = ")
print(np.around(np.mat('4. 12. -16.;12. 37. -43.;-16. -43. 98.'),decimals=3))
print("inv(A) using Cholesky:")
print(np.around(chole.Cholesky(np.mat('4. 12. -16.;12. 37. -43.;-16. -43. 98.')),decimals=3))
print("inv(A) using numpy.linalg.inv:")
print(np.around(np.linalg.inv(np.mat('4. 12. -16.;12. 37. -43.;-16. -43. 98.')),decimals=3))

input()

print("*************Levinson Part*************")
print("Matrix A = ")
print(np.around(np.mat('1. 8. 3. 2. 5. ;8. 1. 8. 3. 2. ;3. 8. 1. 8. 3. ;2. 3. 8. 1. 8. ;5. 2. 3. 8. 1.'),decimals=3))
print("inv(A) using Levinson-Durbin Recursion:")
print(np.around(levin.LevinsonDurbin(np.mat('1. 8. 3. 2. 5. ;8. 1. 8. 3. 2. ;3. 8. 1. 8. 3. ;2. 3. 8. 1. 8. ;5. 2. 3. 8. 1.')),decimals=3))
print("inv(A) using numpy.linalg.inv:")
print(np.around(np.linalg.inv(np.mat('1. 8. 3. 2. 5. ;8. 1. 8. 3. 2. ;3. 8. 1. 8. 3. ;2. 3. 8. 1. 8. ;5. 2. 3. 8. 1.')),decimals=3))