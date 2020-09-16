#Segunda derivada
import numpy as np
from math import factorial as fac
from scipy.integrate import quad

#Generalizada
def bjs(n,h,s,alfa):
    """
    Coeficiente de Laplace generalizado

    Estos son los coeficinetes [n|h]/[s] de D'Eliseo

    Fuente: Maurizio M. D'Eliseo (1989)

    Ej.
      b^(j)_s(a) = bjs(j,0,s,a)
    """
    b=lambda x:np.cos(n*x)*(np.cos(x)-alfa)**h/\
               (1-2*alfa*np.cos(x)+alfa**2)**s
    i,e=quad(b,0,np.pi,epsrel=1e-16)
    return 2*i/np.pi

def Dkbjs(k,j,s,alfa):
    """
    Coeficientes de Laplace y sus derivadas

    Ej.
      b^(j)_s(a) = Dkbjs(a,j,s,0)
      D^k b^(j)_s(a) = Dkbjs(a,j,s,k)

    Fuente: Maurizio M. D'Eliseo (1989)
    """
    d=0
    for h in range(int(k/2)+1):
        p=1
        for i in range(k-h):p*=(s+i)
        f=(-1)**h*2**(k-2*h)*fac(k)/(fac(h)*fac(k-2*h))
        b=bjs(j,k-2*h,s+k-h,alfa)
        d+=f*p*b
    return d

def Dop(Cs,j,s,alfa):
    """
    Calcula el operador:

      [C_0*D^0 + C_1*D^2 + C_2*D^3 + ... ] b^(j)_s(alfa)

    Entradas:
      Cs: [C_0,C_1,C_2,...]
      j: Entero
      s: Semientero
      alfa: argumento del coeficiente

    Salida:
      Calculo del valor del operador en alfa.

    Ejemplos:
      1/2 b^(1)_1/2 (0.5) = Dop([1/2],1,1/2,0.5)
      [2 a D + a^2 D^2] b^(0)_1/2 (a)= Dop([0,2*a,a**2],0,1/2,a)
    """
    suma=0
    for k,C in enumerate(Cs):
        suma+=C*Dkbjs(k,j,s,alfa)
    return suma
