import random as rand
x1_min = -30
x1_max = 20
x2_min = -25
x2_max = 10
x3_min = -30
x3_max = -15
y_max = 5
y_min = -25
exp_matrix = []
y_average = []
y_i = []
exp_matrix_names = ['x₁', 'x₂', 'x₃', 'y₁', 'y₂', 'y₃']
for i in range(4):
    y_norm = []
    for _ in range(3):
        y_norm.append(rand.randint(y_min, y_max))
    y_average.append(sum(y_norm)/5)
    exp_matrix.append(y_norm)
    y_i.append(y_norm)

exp_matrix[0].insert(0, x3_min)
exp_matrix[0].insert(0, x2_min)
exp_matrix[0].insert(0, x1_min)
exp_matrix[1].insert(0, x3_max)
exp_matrix[1].insert(0, x2_max)
exp_matrix[1].insert(0, x1_min)
exp_matrix[2].insert(0, x3_max)
exp_matrix[2].insert(0, x2_min)
exp_matrix[2].insert(0, x1_max)
exp_matrix[3].insert(0, x3_min)
exp_matrix[3].insert(0, x3_max)
exp_matrix[3].insert(0, x3_max)
print(exp_matrix)