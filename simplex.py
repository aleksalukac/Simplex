import numpy as np
from numpy.linalg import inv

b_final = []
b_inv = []

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
        if(min(b_final)):
            return True, indexes
        
        return False, None
        
    for i in range(startIndex, maxIndex - indexesToSelect + 1):
        found, outindexes = GetValidBMatrix(i + 1, maxIndex, indexesToSelect - 1, indexes + [i])
        
        if(found):
            return found, outindexes
#%%

print("Unesite broj parametara")
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

#print(equations)

# %% 

a = np.matrix(equations)

c = np.matrix(params + [0] * number_of_equations)

b = np.matrix(values)
b = b.transpose()
b = -b
#print(np.dot(b, a[:,3]))

# %%

isPossible, indexes = GetValidBMatrix(0, a.shape[1], b.shape[0])
if(not isPossible):
    print("Greska")

c_indexes =  np.matrix([c[0,i] for i in indexes])

# %% generate matrix

matrix = np.append(np.dot(c_indexes, b_inv), b_inv , axis=0)









