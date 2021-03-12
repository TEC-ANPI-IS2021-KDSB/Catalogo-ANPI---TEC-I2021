#include <cmath>
#include <iostream>
#include <ginac/ginac.h>
#include "matplotlibcpp.h"
using namespace std;
using namespace GiNaC;
namespace plt = matplotlibcpp;

ex f(string funct, ex value){
  symbol x;
  symtab table;
  table["x"] = x;
  parser reader(table);
  ex f = reader(funct);
  return evalf(f.subs(x==value));
}

ex * falsa_posicion(string funct,ex startInt, ex endInt, int maxIt, ex tol){
  ex a = startInt;
  ex b = endInt;
  ex xk = a-((a-b)/(f(funct, a)-f(funct, b)))*f(funct, a);
  ex functXk;
  vector<double> graphX(maxIt), graphY(maxIt);
  int i=0;
  static ex r[2];
  ex err = tol+1;
  while(i<maxIt && err>tol){
    functXk = f(funct, xk);
    if(f(funct, a)*functXk<0){
      xk = xk-functXk*(xk-a)/(functXk-f(funct, a));
      // Para la siguiente iteracion
      b = xk;
    }else if(functXk*f(funct, b)<0){
      xk = xk-functXk*(xk-b)/(functXk-f(funct, b));
      // Para la siguiente iteracion
      a = xk;
    }else{
      cout << "No se puede resolver por falsa posicion" << endl;
      return 0;
    }
    // Grafica
    graphX.push_back(i);
    graphY.push_back(ex_to<numeric>(abs(f(funct,xk))).to_double());
    i+=1;
  }
  plt::plot(graphX, graphY);
  plt::show();
  r[0] = evalf(xk);
  r[1] = abs(f(funct, xk));
  return r;
}

int main(void){
  ex *r;
  r = falsa_posicion("cos(x)-x", 1/2, Pi/4, 4, 1e-10); 
  cout << "Aproximacion: " << *r << endl;
  cout << "Error: " << *(r+1) << endl;
}
