import numpy as np
from numpy.linalg import inv

b_final = []
b_inv = []

def FindOptimalIndex(indexes_count, indexes, upper_row):
    
    minVal = 0
    index = -1
    
    for i in range(indexes_count):
        if(i not in indexes):
            temp = np.dot(upper_row, a[:,i])[0, 0] - c[0, i]
            if(temp < minVal):
                minVal = temp
                index = i
    
    return minVal, index

def GetValidBMatrix(startIndex, maxIndex, indexesToSelect, indexes = []):    
    global b_final, b_inv
    
    if(indexesToSelect == 0):
        matrixB = a[:,min(indexes)]

        for i in indexes:
            if(i == min(indexes)):
                continue
            matrixB = np.append(matrixB, a[:,i], axis=1)
        
        b_inv = inv(matrixB)        
        b_final = np.dot(b_inv, b)
        if(min(b_final) >= 0):
            return True, indexes
        
        return False, None
        
    for i in range(startIndex, maxIndex - indexesToSelect + 1):
        found, outindexes = GetValidBMatrix(i + 1, maxIndex, indexesToSelect - 1, indexes + [i])
        
        if(found):
            return found, outindexes

#%%

print("Unesite broj parametara za maksimizaciju")
number_of_params = int(input())

print("Unesite koeficijente za optimizaciju")

params = []
equations = []
values = []

for i in range(number_of_params):
    k = float(input())
    params += [k]   
    
print("Unesite broj nejednacina")
number_of_equations = int(input())

for i in range(number_of_equations):
    print("Unesite koeficijente " + str(i + 1) + ". nejednacine")
    temp_array = []
    
    for j in range(number_of_params):
        k = float(input())
        temp_array += [k]   
    
    temp_array += ([0.0] * i + [1.0] + [0.0] * (number_of_equations - i - 1))
    
    equations += [temp_array]
    
    print("Unesite vrednost od koje je ova nejednacina manja ili jednaka")
    k = float(input())
    values += [-k]
    
# %% 

a = np.matrix(equations)

c = np.matrix(params + [0] * number_of_equations)

b = np.matrix(values)
b = b.transpose()
b = -b

isPossible, indexes = GetValidBMatrix(3, a.shape[1], b.shape[0])

indexes_in_column = []

for i in range(a.shape[1]):
    if(i not in indexes):
        indexes_in_column += [i]

if(not isPossible):
    print("Greska")

c_indexes = np.matrix([c[0,i] for i in indexes])

upper_row = np.dot(c_indexes, b_inv)

matrix = np.append(upper_row, b_inv , axis=0)

to_add = np.append(np.dot(c_indexes, b_final),b_final, axis = 0)
matrix = np.append(matrix, to_add, axis = 1)

# %% 

index = -2

while(index != -1):
    minVal, index = FindOptimalIndex(a.shape[1], indexes, upper_row)
    
    if(index == -1):
        print("Max je " + str(matrix[0,-1]))
        break
    
    temp = np.matrix(a[:, indexes_in_column[index]])
    column_to_add = np.dot(matrix[1:, :-1], temp)
    column_to_add = np.append(np.matrix(minVal), column_to_add, axis = 0)
    
    minDivided = -1
    pivotIndex = -1
    
    for i in range(len(matrix[:,-1])):
        temp = matrix[i, -1] / column_to_add[i]
        
        if(temp > 0):
            if(temp < minDivided or minDivided < 0):
                minDivided = temp
                pivotIndex = i
            
    pivotElement = column_to_add[pivotIndex, 0]
    for i in range(len(matrix[:,0])):
        for j in range(len(matrix[:,0])):
            if(i == pivotIndex):
                continue
            else:
                matrix[i, j] = matrix[i, j] - matrix[pivotIndex, j] * column_to_add[i] / pivotElement
    
    for i in range(len(matrix[:,0])):
        matrix[pivotIndex, i] /= pivotElement
    
    indexes[pivotIndex - 1], indexes_in_column[index] = indexes_in_column[index], indexes[pivotIndex - 1]
    upper_row = matrix[0, 0:-1]
    
"""
IN:
3
6 
14
13

2
0.5
2
1 
24

1
2
4
60

OUT: 294
"""