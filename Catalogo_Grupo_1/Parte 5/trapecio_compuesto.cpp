#include <ginac/ginac.h>
#include <iostream>
#include <math.h>

using namespace std;
using namespace GiNaC;

/** Metodo encargado de evaluar una funcion representada en string en un valor especifico utilizando la libreria GiNaC
* @param funct La funcion que se quiere evaluar en formato de string
* @param value El valor en el cual se va a evaluar la funcion
*/
double f(string funct, double value){
  symbol x;
  symtab table;
  table["x"] = x;
  parser reader(table);
  ex f = reader(funct);
  ex sol = evalf(f.subs(x==value));
  if(!is_a<numeric>(sol)){
    throw logic_error("Se va a intentar convertir un expresion a double que no es numerica");
  } 
  return ex_to<numeric>(sol).to_double();
}

/** Metodo encargado de evaluar una funcion representada en su version simbolica en un valor especifico utilizando la libreria GiNaC
* @param funct La funcion que se quiere evaluar en formato simbolico
* @param value El valor en el cual se va a evaluar la funcion
*/
double f(ex funct, double value, symbol x){
  ex sol = evalf(funct.subs(x==value));
  if(!is_a<numeric>(sol)){
    throw logic_error("Se va a intentar convertir un expresion a double que no es numerica");
  }
  return ex_to<numeric>(sol).to_double();
}
/**
 * Metodo encargado de encontrar la solucion de una ecuacion utilizando Newton-Raphson
 * @param funct La funcion que se quiere evaluar en formato simbolico
 * @param xi Un valor inicial para arrancar el Algoritmo
 * @param iterMax La cantidad maxima de iteraciones a llevar a cabo
 * @param x La variable simbolica
 */
double newtonRaphson(ex funct, double xi, int iterMax, symbol x){
  ex df = funct.diff(x);
  cout << df << endl;
  cout << funct << endl;
  ex xk = xi;
  for (int i = 0; i < iterMax; i++){
    if(evalf(df.subs(x==xk)) <= 1e-8){
      break;
    }
    xk = xk - funct.subs(x==xk)/df.subs(x==xk);
  }
  // Retornando
  if(!is_a<numeric>(xk)){
    throw logic_error("Se va a intentar convertir una expresion a double que no es numerica");
  }
  double sol = ex_to<numeric>(xk).to_double();
  return sol;
}

/**
 * Metodo encargado de retornar la version simbolica de una funcion
 * @param funct La funcion que se quiere evaluar en formato de string
 * @returns La funcion simbolica representada por el string ingresado
 */ 
ex fSym(string funct, symbol x){
  symtab table;
  table["x"] = x;
  parser reader(table);
  ex f= reader(funct);
  return f;
}

/**
 * Metodo encargado de calcular el máximo de una funcion dado un intervalo
 * @param funct La funcion que se quiere evaluar en formato de string
 * @param x La variable simbolica
 * @param a Inicio del intervalo
 * @param b Final del intervalo
 */
double maxFun(ex funct, symbol x, double a, double b){
  ex befConv; // Esta variable se va a usar para verificar si las expresiones que se van a convertir a double son numericas
  ex f= funct; // Funcion
  ex df = f.diff(x); // Funcion diferenciada

  // Primero se tiene que calcular cuándo la derivada es 0
  double valorLimite = newtonRaphson(funct, (a+b)/2, 500, x);

  // Luego se valua donde la derivada da 0 y en los limites
  vector<double> posibles = {};

  if(!(valorLimite < a || valorLimite > b)){ // Si el valor limite se encuentra en el rango..
    befConv = evalf(f.subs(x==valorLimite)); 
    posibles.push_back(
      abs(ex_to<numeric>(befConv).to_double())
    );
  }

  befConv = evalf(f.subs(x==a)); 
  posibles.push_back(
    abs(ex_to<numeric>(befConv).to_double())
    );
  befConv = evalf(f.subs(x==b));
  posibles.push_back(
    abs(ex_to<numeric>(befConv).to_double())
    );
  double max = posibles[0];
  // Ahora se debe encontrar el mayor número dentro de 'posibles'
  for(int i = 0; i < posibles.size(); i++){
    if(posibles[i]>max){
      max = posibles[i];
    }
  }
  
  if(!is_a<numeric>(max)){
    throw logic_error("Se va a intentar convertir una expresion a double que no es numerica");
  }

  return ex_to<numeric>(max).to_double();
}

/**
 * Método que calcula una aproximacion de la integral de una funcion 
 * A partir el método del trapecio compuesto. Se asume que la funcion
 * Ingresada es dos veces derivable
 * @param funct Funcion a evaluar en formato de string
 * @param puntos Cantidad de puntos en los que se va a dividir el intervalo
 * @param a Inicio del intervalo de integracion
 * @param b Final del intervalo de integracion
 * @return Imprime la aproximacion de la integral junto con su error, ademas devuelve la aproximacion de la integral
*/
double trapecio_compuesto(string funct, int puntos, double a, double b){
  symbol x("x");

  vector<double> s = {};
  double espacio = (b-a)/(puntos-1);
  double i = a;
  while (i<=b){
    s.push_back(i);
    i = i+espacio;
  }

  ex diff2 = fSym(funct,x).diff(x,2);

  double h = s[2]-s[1];
  double sum = 0;
  i = 0;
  while (i<=puntos-2){
    sum = sum + f(funct,s[i]) + f(funct,s[i+1]);
    i=i+1;
  }
  double alph=maxFun(fSym(funct, x).diff(x,2), x, a, b); 
  double power = ex_to<numeric>((GiNaC::pow(h,2))).to_double();
  double aprox = (h/2)*sum;
  double err = power*((b-a)/12)*alph;

  cout << "La aproximacion es: " << aprox << endl;
  cout << "Con error: " << err << endl;

  return aprox;
}


/**
 * Ejemplo Numérico
 */
int main (int argc, char const* argv[]){
  trapecio_compuesto("log(x)", 4,2,5);
  return 0;
}