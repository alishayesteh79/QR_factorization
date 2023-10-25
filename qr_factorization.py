import numpy as np

# inputing the matrix
rows = int(input('\nEnter the number of rows:'))
cols = int(input('\nEnter the number of columns:'))
print('\nenter the entries of matix in a single line (seprated by an space)')
entries = list(map(int, input().split()))

# initialing the matrices
matrix = np.array(entries)
matrix = matrix.reshape(rows, cols)
print(f'\ninputed matrix is :\n{matrix}')

q = np.zeros(shape=(rows, cols))
r = np.zeros(shape=(cols,cols))

q[:,0] = matrix[:,0]
r[0,0] = 1

#quantification of matrices r and q
for j in range(1,cols):
    for i in range(cols):
        if i == j :
            r[i,j] = 1
            sum = np.zeros(shape=(1,rows))

            for k in range(j):
               sum = sum + r[k,j]*q[:,k]
            q[:,j] = matrix[:,j] - sum
            break

        else:
            r[i,j] = np.dot(matrix[:,j], q[:,i]) / (np.linalg.norm(q[:,i])**2)

# computing matrices D and Dinv
D = np.zeros(shape=(cols, cols))
Dinv = np.zeros(shape=(cols, cols))

for i in range(cols):
    a = np.linalg.norm(q[:,i])
    D[i,i] = a
    Dinv[i,i] = 1/a

#computing final matrices Q and R
R = np.dot(D,r)
Q =np.dot(q,Dinv)

# printing the result
print(f'\nmatrix Q is :\n{Q}')
print(f'\nmatrix R is :\n{R}')