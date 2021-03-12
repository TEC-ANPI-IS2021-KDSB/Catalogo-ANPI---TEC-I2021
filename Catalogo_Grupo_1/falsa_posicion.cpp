#include <cmath>
#include <iostream>
#include <ginac/ginac.h>
using namespace std;
using namespace GiNaC;

ex f(string funct, ex value){
  symbol x;
  symtab table;
  table["x"] = x;
  parser reader(table);
  ex f = reader(funct);
  return evalf(f.subs(x==value));
}

ex * falsa_posicion(string funct,ex startInt, ex endInt, int maxIt){
  ex a = startInt;
  ex b = endInt;
  ex xk = a-((a-b)/(f(funct, a)-f(funct, b)))*f(funct, a);
  ex functXk;
  int i=0;
  static ex r[2];
  while(i<maxIt){
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
    i+=1;
  }
  r[0] = evalf(xk);
  r[1] = abs(f(funct, xk));
  return r;
}

int main(void){
  ex *r;
  r = falsa_posicion("cos(x)-x", 1/2, Pi/4, 4); 
  cout << "Aproximacion: " << *r << endl;
  cout << "Error: " << *(r+1) << endl;
}
