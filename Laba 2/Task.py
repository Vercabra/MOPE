import random as rand
from prettytable import PrettyTable

x1_min = -30
x1_max = 20
x2_min = -25
x2_max = 10
y_max = -2750
y_min = -2850
exp_matrix = []
y_average = []
y_i = []
exp_matrix_names = ['x1', 'x2', 'y1', 'y2', 'y3', 'y4', 'y5']
for i in range(3):
    y_norm = []
    for _ in range(5):
        y_norm.append(rand.randint(y_min, y_max))
    y_average.append(sum(y_norm)/5)
    exp_matrix.append(y_norm)
    y_i.append(y_norm)


exp_matrix[0].insert(0, -1.0)
exp_matrix[0].insert(0, -1.0)
exp_matrix[1].insert(0, 1.0)
exp_matrix[1].insert(0, 1.0)
exp_matrix[2].insert(0, -1.0)
exp_matrix[2].insert(0, 1.0)

exp_table = PrettyTable()
exp_table.field_names = exp_matrix_names
exp_table.add_rows(exp_matrix)
print('Normed matrix of experiment:')
print(exp_table)

sigma_y1 = 0.2 * ((y_i[0][0] - y_average[0])**2 + (y_i[0][1] - y_average[0])**2 + (y_i[0][2] - y_average[0])**2 +
                  (y_i[0][3] - y_average[0])**2 + (y_i[0][4] - y_average[0])**2)

sigma_y2 = 0.2 * ((y_i[1][0] - y_average[1])**2 + (y_i[1][1] - y_average[1])**2 + (y_i[1][2] - y_average[1])**2 +
                  (y_i[1][3] - y_average[1])**2 + (y_i[1][4] - y_average[1])**2)

sigma_y3 = 0.2 * ((y_i[2][0] - y_average[2])**2 + (y_i[2][1] - y_average[2])**2 + (y_i[2][2] - y_average[2])**2 +
                  (y_i[2][3] - y_average[2])**2 + (y_i[2][4] - y_average[2])**2)

sigma_main = 1.79

R_uv1 = abs(sigma_y1 / sigma_y2 * 0.6 - 1)/sigma_main
R_uv2 = abs(sigma_y3 / sigma_y1 * 0.6) / sigma_main
R_uv3 = abs(sigma_y3 / sigma_y2 * 0.6) / sigma_main
print('\nDetermination of homogeneous of dispersion:')
print('    σ²{y₁}:', sigma_y1)
print('    σ²{y₂}:', sigma_y2)
print('    σ²{y₃}:', sigma_y3)
print('    Rᵤᵥ₁:', R_uv1)
print('    Rᵤᵥ₂:', R_uv2)
print('    Rᵤᵥ₃:', R_uv3)
if R_uv1 < 2 and R_uv2 < 2 and R_uv3 < 2:
    print('    Dispersion is homogeneous ')


