#include <cmath>
#include <iostream>
using namespace std;

double f(x){
  return x;
}

double * falsa_posicion(double startInt, double endInt, int maxIt){
  double a = startInt;
  double b = endInt;
  double xk = a-((a-b)/(f(a)-f(b)))*f(a);
  int i=0;
  double r[2];
  while(i<maxIt){
    if(f(a)*f(xk)<0){
      xk = xk-f(xk)*(xk-a)/(f(xk)-f(a));
      // Para la siguiente iteracion
      b = xk;
    }else if(f(xk)*f(b)<0){
      xk = xk-f(xk)*(xk-b)/(f(xk)-f(b));
      // Para la siguiente iteracion
      a = xk;
    }else{
      cout << "No se puede resolver por falsa posicion" < endl;
      return 0;
    }
    i+=1;
  }
  r[0] = xk;
  r[1] = f(xk);
  return r;
}

int main(void){

}
