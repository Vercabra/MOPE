import random as rand
import numpy as np
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
exp_matrix_names = ['x₁', 'x₂', 'y₁', 'y₂', 'y₃', 'y₄', 'y₅']
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

mx1 = 1/3
mx2 = -1/3
my = sum(y_average)/3
a1 = 1
a2 = 1/3
a3 = 1
a11 = (-1 * y_average[0] + 1 * y_average[1] + 1 * y_average[2]) * (1 / 3)
a22 = (-1 * y_average[0] + 1 * y_average[1] + -1 * y_average[2]) * (1 / 3)
b_01 = np.array([[my, mx1, mx2], [a11, a1, a2], [a22, a2, a3]])
b_02 = np.array([[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])
b_11 = np.array([[1, my, mx2], [mx1, a11, a2], [mx2, a22, a3]])
b_21 = np.array([[1, mx1, my], [mx1, a1, a11], [mx2, a2, a22]])

b0 = round(np.linalg.det(b_01)/np.linalg.det(b_02), 2)
b1 = round(np.linalg.det(b_11)/np.linalg.det(b_02), 2)
b2 = round(np.linalg.det(b_21)/np.linalg.det(b_02), 2)

y_regression = [round(b0 - b1 - b2, 4), round(b0 + b1 + b2, 4),  round(b0 + b1 - b2, 4)]
print('\nNormed equation of regression: y = {} + {}x₁ + {}x₂'.format(b0, b1, b2))
print('y average:', y_average)
print("y regression's:", y_regression)

delta_x1 = abs(x1_max - x2_min)/2
delta_x2 = abs(x1_max - x2_min)/2
x10 = (x1_max + x1_min)/2
x20 = (x2_max + x2_min)/2
a0 = b0 - b1*(x10 / delta_x1) - b2*(x20/delta_x2)
a1 = b1/delta_x1
a2 = b2/delta_x2
y_norm_regression = [round(a0 + x1_min * a1 + x2_min * a2, 4), round(a0 + x1_max * a1 + x2_max * a2, 4),
                     round(a0 + x1_max * a1 + x2_min * a2, 4)]

print('\nNormed equation of regression: y = {} + {}x₁ + {}x₂'.format(round(a0, 2), round(a1, 2), round(a2, 2)))
print("y normed regression's:", y_norm_regression)
