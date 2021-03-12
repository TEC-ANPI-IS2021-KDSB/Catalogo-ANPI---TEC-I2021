#include <iostream>
#include <ginac/ginac.h>
using namespace std;
using namespace GiNaC;

ex prueba(string funct, double value){
  symbol x;
  symtab table;
  table["x"] = x;
  parser reader(table);
  ex f = reader(funct);
  return evalf(f.subs(x==value));
}

int main(){
  symbol x("x");
  ex a;
  a = pow(Pi,2)+x;
  cout << a << " becomes " << a.subs(x==1) << endl;
  cout << evalf(a.subs(x==1)) << endl;
  cout << "Ahora en una funcion" << endl;
  cout << prueba("cos(2*x)^2-x^2", 1) << endl;
  return 0;
}
