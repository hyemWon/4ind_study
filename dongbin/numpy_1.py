# Numpy 배열 차원 이해

import numpy as np

# array = np.arange(0,10).reshape(2,5)
# print(array)

# # 3차원 텐서
array2 = np.arange(0,24).reshape(4,3,2)
print(array2)

# array = np.arange(0,6).reshape(3,2)
# print(array)
# print(array.sum(axis=0))
# print(array.sum(axis=1))

print(array2.sum(axis=0))
