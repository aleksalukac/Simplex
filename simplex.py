import numpy as np

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
    print("Unesite koeficijente " + str(i + i) + ". nejednacine")
    temp_array = []
    
    for j in range(number_of_params):
        k = float(input())
        temp_array += [k]   
    
    temp_array += ([0.0] * i + [1.0] + [0.0] * (number_of_equations - i - 1))
    
    equations += [temp_array]
    
    print("Unesite vrednost od koje je ova nejednacina manja ili jednaka")
    k = float(input())
    values += [k]

print(equations)