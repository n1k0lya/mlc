import numpy as np

firstnp = np.array([1, 2, 3, 4, 5])
snp = np.full((10,), 0)
tnp = np.full((3,4), 1)
fnp = np.arange(0, 20)
print(firstnp)
print(snp)
print(fnp)
print(tnp)
print(tnp.shape)
print(tnp.dtype)

print(fnp[5:10])
print(fnp[::2])
print(fnp[-3:])

fnp = fnp.reshape(4, 5)
print(fnp[2, 3])
print(fnp[0,:])
print(fnp[:,1])
print(fnp[1:1+2, 1:1+2])


n = np.arange(1,6)
print(n*2)
print(n**2)
print(n+10)
print(np.sqrt(n))

l = np.array([[4, 5, 6],
              [7,8,9]])
v = np.array ([[10, 9, 8],
               [4,5,6]])

print(l+v)
print(l*v)
print(l>v)

mnp = np.arange(0,20)
print(np.sum(mnp))
print(np.mean(mnp))
print(np.max(mnp))
print(np.min(mnp))
print(np.std(mnp))

print(np.sum(fnp[1,:]))
print(np.sum(fnp[:,1]))

exe = np.array([[1,2,3, 4],
                [5,6,7,8],
                [9,10,11,12]])

lex = np.array([1,2,3,4])

esh = exe+lex
mf = esh.mean(axis = 0)
ol = esh - mf


matr = np.random.rand(5, 3)
wes = np.random.rand(3, )
y_pred = matr @ wes
print(y_pred)