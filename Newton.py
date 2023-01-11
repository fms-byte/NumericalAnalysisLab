import math

def Newton(f,f1,p0,TOL,N0):
    i=0;
    while i<=N0:
        p = p0-f(p0)/f1(p0);
        print(format(i,'3d'),'  ',format(p0,'10.8f'),'  ',format(abs(p-p0),'10.2e'));
        if abs(p-p0)< TOL:
            return print('The solution is ', p);
        i=i+1;
        p0=p;
    print('The method fails after N0 iterations');
    return None

#f = lambda x: x*math.sin(x) + math.cos(x);
#f1 = lambda x: x*math.cos(x);

f= lambda x: x*math.exp(x) -1
f1= lambda x: (x+1)*math.exp(x)
Newton(f, f1, 1, 0.0000000000000001, 20)
