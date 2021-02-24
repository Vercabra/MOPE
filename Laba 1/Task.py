import random as rand
from prettytable import PrettyTable

a0 = 5
a1 = 12
a2 = 8
a3 = 11

experiment_matrix = [['№', 'X1', 'X2', 'X3', 'Y', 'Xn1', 'Xn2', 'Xn3']]
X1_arr = []
X2_arr = []
X3_arr = []
Y_arr = []

for i in range(8):
    X1_arr.append(rand.randint(1, 20))
    X2_arr.append(rand.randint(1, 20))
    X3_arr.append(rand.randint(1, 20))
    Y_arr.append(a0 + a1 * X1_arr[i] + a2 * X2_arr[i] + a3 * X3_arr[i])
    experiment_matrix.append([i+1, X1_arr[i], X2_arr[i], X3_arr[i], Y_arr[i]])

x0_arr = ['x0', (max(X1_arr) + min(X1_arr)) / 2, (max(X2_arr) + min(X2_arr)) / 2, (max(X3_arr) + min(X3_arr)) / 2]
Y_et = a0 + a1 * x0_arr[1] + a2 * x0_arr[2] + a3 * x0_arr[3]
x0_arr.append(Y_et)
for i in range(3):
    x0_arr.append(' ')

experiment_matrix.append(x0_arr)

dx_arr = ['dx', x0_arr[1] - min(X1_arr), x0_arr[2] - min(X2_arr), x0_arr[3] - min(X3_arr)]
experiment_matrix.append(dx_arr)
for i in range(4):
    dx_arr.append(' ')
Xn1_arr = []
Xn2_arr = []
Xn3_arr = []

for i in range(8):  # cycle which append X_i_normed in main matrix (i for each factor)
    experiment_matrix[i + 1].append(round((X1_arr[i] - x0_arr[1])/dx_arr[1], 3))
    experiment_matrix[i + 1].append(round((X2_arr[i] - x0_arr[2]) / dx_arr[2], 3))
    experiment_matrix[i + 1].append(round((X3_arr[i] - x0_arr[3]) / dx_arr[3], 3))

choice_Y = []
for i in range(len(Y_arr)):
    choice_Y.append([(Y_arr[i]-Y_et)**2, i])

chosen_y = max(choice_Y, key=lambda x: x[0])[1]

experiment_table = PrettyTable()
experiment_table.field_names = experiment_matrix[0]
for i in range(1, len(experiment_matrix)):
    experiment_table.add_row(experiment_matrix[i])
print(experiment_table)
print("Criterion for selecting optimality's arguments is №{} : {}, {}, {}".format(chosen_y + 1, X1_arr[chosen_y],
                                                                                  X2_arr[chosen_y], X3_arr[chosen_y]))
