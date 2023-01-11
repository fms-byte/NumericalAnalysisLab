#n = 5;
# x = [1.0, 1.3, 1.6, 1.9, 2.2];
# y = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
n=4
x = [300, 304, 305, 307]
y = [2.4771, 2.4829, 2.4843, 2.4871]

# input the value of interpolation
value = 301;
p = 0;
for i in range(n):
    L = 1;
    for k in range(n):
        if i != k:
            L = L * (value - x[k]) / (x[i] - x[k]);
    p = p + y[i] * L;
print('\n Value at', value, 'is', round(p, 9));
