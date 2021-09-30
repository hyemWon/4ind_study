# 동빈나파이썬 이미지처리
# 넘파이 Numpy
# 다차원 배열을 효과적으로 처리할 수 있도록 도와주는 도구
# 현실 세계의 다양한 데이터는 배열 형태로 표현 가능
# list에 비해 빠르고 강력한 기능 제공

import numpy as np

# list_data = [1,2,3]
# array = np.array(list_data) #numpy 자료형으로 변환
# print(array)
# print(array.size)
# print(array.dtype)
# print(array[2])

# array1 = np.arange(4)
# print(array1)

# array2 = np.zeros((4,4), dtype=float)
# print(array2)

# array3 = np.ones((3,3), dtype=str)
# print(array3)

# 0부터 9까지 랜덤하게 초기화
# for i in range(10):
#     array4 = np.random.randint(0, 10, (3,3))
#     print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열 (표준정규분포)
# array5 = np.random.normal(0, 1, (3,3))
# print(array5)

# 배열 합치기
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])
# array3 = np.concatenate([array1, array2])

# print(array3.shape)
# print(array3)

# array1 = np.array([1,2,3,4])
# array2 = array1.reshape((2,2))
# print(array2)

# array1 = np.arange(4).reshape(1,4)
# array2 = np.arange(8).reshape(2,4)
# # print(array1)
# print(array2)

# # array3 = np.concatenate([array1, array2], axis=0)
# # print(array3)
# left, right = np.split(array2, [2], axis=1)
# print(left)
# print(right)

# array = np.random.randint(1, 10, size=4).reshape(2,2)
# print(array)

# result_array = array * 10
# print(result_array)

# 서로 다른 형태의 배열을 연산할 때는 행 우선으로 수행된다.(Broad casting)
# array1 = np.arange(4).reshape(2,2)
# array2 = np.arange(2)
# array3 = array1 + array2

# print(array1)
# print(array2)
# print(array3)

# array1 = np.arange(0, 8).reshape(2,4)
# array2 = np.arange(0, 8).reshape(2,4)
# array3 = np.concatenate([array1, array2], axis=0)
# array4 = np.arange(0, 4).reshape(4,1)
# array5 = array3 + array4
# print(array3)
# print(array4)
# print(array5)

# 마스킹 연산 : 각 원소에 대해 체크 (조건문보다 훨씬 빠름)
# array1 = np.arange(16).reshape(4,4)
# print(array1)

# array2 = array1 < 10
# print(array2)

# array1[array2] = 100
# print(array1)

# array = np.arange(16).reshape(4,4)
# print(array)
# print("최대값: ", np.max(array))
# print("최소값: ", np.min(array))
# print("합계: ", np.sum(array, axis=0))
# print("합계: ", np.sum(array, axis=1))
# print("평균값: ", np.mean(array))


# 단일 객체 저장 및 불러오기
# array = np.arange(0,10)
# np.save('saved.npy', array)

# result = np.load('saved.npy')
# print(result)

# 복수 객체 저장 및 불러오기
# array1 = np.arange(0, 10)
# array2 = np.arange(10, 20)
# np.savez('saved.npz', a1=array1, a2=array2)

# data = np.load('saved.npz')
# print(data)
# result1 = data['a1']
# result2 = data['a2']
# print(result1)
# print(result2)


# Numpy 원소 오름차순 정렬
# array = np.array([5,9,10,3,1])
# array.sort()
# print(array)
# 내림차순 정렬
# print(array[::-1])

# 각 열을 기준으로 정렬
# array = np.array([[5,9,10,3,1], [8,3,4,2,5]])
# print(array)
# array.sort(axis=0)
# print(array)

# 균일한 간격으로 데이터 생성
# array = np.linspace(0, 10, 5)
# print(array)

# 난수의 재연 (실행마다 결과 동일)
# np.random.seed(7)
# print(np.random.randint(0, 10, (2,3)))

# 복사
# array1 = np.arange(0,10)
# array2 = array1.copy()
# array2[0] = 99
# print(array1)
# print(array2)

# 중복된 원소 제거
# array = np.array([1,1,2,2,2,3,3,4])
# print(np.unique(array))