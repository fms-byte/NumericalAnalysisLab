# Simpson's 1/3 Rule

# Define function to integrate
"""def f(x):
    #return 1 / (1 + x ** 2)
    return (1 - x**2)**0.5"""


# Implementing Simpson's 1/3
#def simpson13(x0, xn, n):
def simpson13(f,x0,xn,n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        xi = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(xi)
        else:
            integration = integration + 4 * f(xi)

    # Finding final integration value
    integration = integration * h / 3

    return integration


# Input section
#lower_limit = float(input("Enter lower limit of integration: "))
#upper_limit = float(input("Enter upper limit of integration: "))
#sub_interval = int(input("Enter number of sub intervals: "))

# Call simpson13() method and get result

def simpson38(f,x0,xn,n):
    h=(xn-x0)/n
    integration= f(x0)+f(xn)
    for i in range (1,n):
        xi=x0+i*h
        if i%3==0:
            integration= integration + 2*f(xi)
        else:
            integration= integration + 3*f(xi)
    integration=integration * 3*h/8
    return integration

f= lambda x: (1 - x**2)**0.5
a=0
b=1
n=50
result= simpson38(f,a,b,n)
print("Integration result by Simpson's 3/8 method is: %0.9f"% (result))
#result = simpson13(lower_limit, upper_limit, sub_interval)
result= simpson13(f,a,b,n)
print("Integration result by Simpson's 1/3 method is: %0.9f"% (result))

