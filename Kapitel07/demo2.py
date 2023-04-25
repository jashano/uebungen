import numpy as np

a = np.array([1,2,3,4], dtype=np.float64)
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)

if 50 in b:
    print("50 kommt in der matrix b vor!")
else:
    print("schade")

print(b[1,:])

c=np.zeros([4,4])
c[0,1]=5
print(c)

d=np.arange(1,10,0.1)
print(d)