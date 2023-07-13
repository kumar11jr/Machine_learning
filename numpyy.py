import numpy as np
import time
import sys



# l = range(1000)
# print(sys.getsizeof(5)* len(l))


# array = np.arange(1000)
# print(array.size*array.itemsize)




# size = 100000000

# # python list
# l1 = range(size)
# l2 = range(size)


# # numpy array
# a1 = np.arange(size)
# a2 = np.arange(size)

# start = time.time()
# result = [(x+y) for x,y in zip(l1,l2)]
# print("python list time : ",(time.time()-start)*1000)


# start=time.time()
# result = a1+a2
# print("numpy arr time: ",(time.time()-start)*1000)







# a = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)
# print(a.ndim)  ## dimension of array
# print(a.itemsize)  ## 4 because it is interger array
# print(a.dtype)  ## int32   and if float the float64
# print(np.zeros((3,4)))
# print(np.ones((3,4)))
# print(a.ravel())







n = np.array([7,6,5,4])
print(n[0:2])
print(n[-1])

b1 = np.arange(0,6).reshape(3,2)
b2 = np.arange(6,12).reshape(3,2)

# print(np.vstack((b1,b2)))
# print(np.hstack((b1,b2)))
for row in b1:
    print(row)

for row in b1:
    for cell in row:
        print(cell)
        
for cell in b1.flatten():
    print(cell)
    
# or used npiter for printing********************************************

# b3 = b1>3
# print(b3)
# print(b1[b3])
