import math
from decimal import *
import decimal
decimal.getcontext().prec = 15
tol = decimal.Decimal(float("1e-6"))
itmax = 50
step = decimal.Decimal(float("1e-3"))

def f(x,y):
    result = decimal.Decimal((x**2 + y - 11)**2 + (x + y**2 - 7)**2)
    return result;

def dx(x,y):
    _dx = decimal.Decimal(4*x**3 + 4*x*y - 42*x + 2*y**2 - 14)
    return _dx;

def dy(x,y):
    _dy = decimal.Decimal(2*x**2 +4*x*y + 4*y**3 - 26*y - 22)
    return _dy;

def norm(x,y):
    n2 = decimal.Decimal(x**2 + y**2)
    return math.sqrt(n2);

def g(a,x,y,g,h): #g = dx h = dy
    return decimal.Decimal(4*(a**3)*(g**4)+4*(a**3)*(h**4)-12*(a**2)*(g**3)*x-6*(a**2)*(g**2)*h-6*(a**2)*g*(h**2)-12*(a**2)*(h**3)*y+12*a*(g**2)*(x**2)+4*a*(g**2)*y-42*a*(g**2)+8*a*g*h*x+8*a*g*h*y+4*a*(h**2)*x+12*a*(h**2)*(y**2)-26*a*(h**2)-4*g*(x**3)-4*g*x*y+42*g*x-2*g*(y**2)+14*g-2*h*(x**2)-4*h*x*y-4*h*(y**3)+26*h*y+22*h);

def fa(x,y):
   
    a = decimal.Decimal(0.0)
    b = decimal.Decimal(0.01)
    p_0 = tol + decimal.Decimal(0.10)
    p = decimal.Decimal(0.0)
    norm = tol + decimal.Decimal(0.1)

    while (f(decimal.Decimal(x) - a*(dx(x,y)), decimal.Decimal(y) - a*(dy(x,y))) > f(decimal.Decimal(x) - b*(dx(x,y)), decimal.Decimal(y) - b*(dy(x,y)))):
        b = b*decimal.Decimal(2.0)
    #Achando o Intervalo 
    j = 0
    while ((norm > tol) & (j < itmax)):
        #inicio posicao falsa
        j = j + 1
        p_0 = p #Salva p anterior
        
        #fa = f(decimal.Decimal(x) - a*(dx(x,y)),decimal.Decimal(y) - a*(dy(x,y)))
        #fb = f(decimal.Decimal(x) - b*(dx(x,y)),decimal.Decimal(y) - b*(dy(x,y)))
        fa = g(a, x,y, dx(x,y), dy(x,y))
        fb = g(b, x,y, dx(x,y), dy(x,y))

        p = decimal.Decimal(a - ((fa*(b-a))/(fb-fa)))
        
        fp = g(p, x,y, dx(x,y), dy(x,y))#f(decimal.Decimal(x) - p*(dx(x,y)),decimal.Decimal(y) - p*(dy(x,y)))
        
        if ( fa*fp < 0):
            b = p
        else:
            a = p

        norm = abs(fp)
            #print "i = %d a= %6.7f b = %6.7f norm = %6.7f fa = %6.15f fb = %6.15f" % (j, a, b, norm, fa, fb )
        
    return decimal.Decimal(p), j
#Fim da posicoo falsa 

a = decimal.Decimal(4)
b = decimal.Decimal(-2)
i = 0
while ( norm(dx(a,b),dy(a,b)) > tol) & (i < itmax):
    i = i + 1
    step, na = fa(a,b)
    a = a - step*(dx(a,b))
    b = b - step*(dy(a,b))
#    print "interations = %d f(x,y)= %6.15f  Grad = %6.15f %6.15f  a = %6.15f x = %6.15f y = %6.15f na = %2d" % (i, f(a,b), dx(a,b), dy(a,b), step, a, b, na)
    print "%2d,%6.15f,%6.15f,%6.15f,%6.15f,%6.15f,%6.15f,%2d" % (i, f(a,b), dx(a,b), dy(a,b), step, a, b, na)
quit()


