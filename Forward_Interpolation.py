def u_cal(u, n):
    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;


def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;


n = 6;
# x = [45, 50, 55, 60];
x = [15, 20, 25, 30, 35, 40];

# y[][] is used for difference table
# with y[][0] used for input

y = [[0 for i in range(n)] for j in range(n)];
y[0][0] = 0.2588190;
y[1][0] = 0.3420201;
y[2][0] = 0.4226183;
y[3][0] = 0.5000010;
y[4][0] = 0.5735764;
y[5][0] = 0.6427876;

# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];

    # Displaying the forward difference table
for i in range(n):
    print(x[i], end="\t");
    for j in range(n - i):
        print(y[i][j], end="\t");
    print("");

# Value to interpolate at
value = 38;

# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);

print("\nValue at", value, "is", round(sum, 6));
