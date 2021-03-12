#include <iostream> 
#include <cmath>
#include <ginac/ginac.h>
using namespace std;
using namespace GiNaC;

ex f(string funct, ex value){
  symbol x;
  symtab table;
  table["x"]=x;
  parser reader(table);
  ex f = reader(funct);
  return evalf(f.subs(x==value));
}

/**
* @param x0 First initial value
* @param x1 Second initial value
* @param maxIt Max Iterations for the function
* @param tol Tolerancia de la funcion
* @param funct Funcion a evaluar
*/
ex * secante(double x0, double x1, int maxIt, string funct, double tol){
  ex xk;
  ex xkm1;
  ex xkp1;
  int i=0;
  ex r[2]; // Array de resultado
  while(i<maxIt){
    // Nuevo resultado
    xkp1 = xk-f(funct,xk)*(xk-xkm1)/(f(funct,xk)-f(funct,xkm1));
    // Reasignando valores para la siguiente iteracion
    xkm1 = xk;
    xk = xkp1;
    // Contador de iteracion
    i+=1;
  }
  r[0] = xk; // Aproximacion
  r[1] = abs(f(funct,xk)); // Error
  return r;
}

int main(void)
{
  cout << secante(0.75,0.437193, 5, "cos(2*x)^2-x^2",1) <<endl;
  return 0;
}
