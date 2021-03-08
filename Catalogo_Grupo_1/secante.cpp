#include <iostream> 
#include "symbolicc++.h"
#include <cmath>
using namespace std;

double f(double x){
  return x;
}

/**
* @param x0 First initial value
* @param x1 Second initial value
* @param maxIt Max Iterations for the function
*/
double * secante(double x0, double x1, int maxIt){
  int xk;
  int xkm1;
  int xkp1;
  int r[2]; // Array de resultado
  while(i<maxIt){
    // Nuevo resultado
    xkp1 = xk-f(xk)*(xk-xkm1)/(f(xk)-f(xkm1));
    // Reasignando valores para la siguiente iteracion
    xkm1 = xk;
    xk = xkp1;
    // Contador de iteracion
    i+=1;
  }
  r[0] = xk; // Aproximacion
  r[1] = abs(f(xk)); // Error
  return r;
}

int main(void)
{
  cout << "a";
  return 0;
}
