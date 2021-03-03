//Se importan las librerias a utilizar.
#include <iostream>
#include <math.h>
//Fin de la importacion de librerias.
using namespace std;

double aprox_div(double a, double tol){
  // Esta funcion aproxima numericamente el valor de 1/a, donde a es diferente de 0
  // Parametros de entrada: a=valor para aproximar su inverso multiplicativo
  //                        tol=tolerancia
  // Parametros de salida:  y=aproximacion numerica de 1/a
    if (a==0){
        double x = 0;
        return x;
    }
    else{
        double error=tol+1;
        double x=0.1;
        while(error>tol){
          double x_new=x*(2-a*x);
          error=abs(x-x_new);
          x=x_new;
        }
        return x;
    }
}

int main(){
  // Ejemplo Numerico
    double a=7;
    double tol=0.0000001;
    double y = aprox_div(a, tol);
    if (y==0){
        cout<<"El valor 1/0 no esta definido"<<endl;
    }
    else{
        cout<<y<<endl;
    }
    return 0;
}
