import math
f = lambda x: x*math.exp(x);
h = 0.1;
x0 = 2.0;

# Three-point endpoint formula
Df_x0 = (-3*round(f(x0),6)+4*round(f(x0+h),6)-round(f(x0+2*h),6))/(2*h);
print('The derivative of f at x0 (By three-point endpoint formula):\n', round(Df_x0,6));


# Three-point midpoint formula
Df_x0 = (round(f(x0+h),6)-round(f(x0-h),6))/(2*h);
print('The derivative of f at x0 (By three-point midpoint formula):\n',  round(Df_x0,6));
#print('The derivative of f at x0 (By three-point midpoint formula):\n',  format(Df_x0,'>12.2e'));


#Five-point endpoint formula
Df_x0= (-25*round(f(x0),6)+48*round(f(x0+h),6)-36*round(f(x0+2*h),6)+16*round(f(x0+3*h),6)-3*round(f(x0+4*h),6))/(12*h);
print('The derivative of f at x0 (By Five-point Endpoint formula):\n',  round(Df_x0,6));


#Five-point midpoint formula
Df_x0= (round(f(x0-2*h),6)-8*round(f(x0-h),6)+8*round(f(x0+h),6)-round(f(x0+2*h),6))/(12*h);
print('The derivative of f at x0 (By Five-point Midpoint formula):\n',  round(Df_x0,6));