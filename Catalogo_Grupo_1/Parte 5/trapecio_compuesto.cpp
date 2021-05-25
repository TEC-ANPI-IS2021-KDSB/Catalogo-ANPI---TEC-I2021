#include <ginac/ginac.h>
#include <iostream>

using namespace std;
using namespace GiNaC;

/** Metodo encargado de evaluar una funcion representada en string en un valor especifico utilizando la libreria GiNaC
* @param funct La funcion que se quiere evaluar en formato de string
* @param value El valor en el cual se va a evaluar la funcion
*/
ex f(string funct, ex value){
  symbol x;
  symtab table;
  table["x"] = x;
  parser reader(table);
  ex f = reader(funct);
  return evalf(f.subs(x==value));
}

/** Metodo encargado de evaluar una funcion representada en su version simbolica en un valor especifico utilizando la libreria GiNaC
* @param funct La funcion que se quiere evaluar en formato simbolico
* @param value El valor en el cual se va a evaluar la funcion
*/
ex f(ex funct, ex value, symbol x){
  return evalf(funct.subs(x==value));
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
 * Método que calcula una aproximacion de la integral de una funcion 
 * A partir el método del trapecio compuesto. Se asume que la funcion
 * Ingresada es dos veces derivable
 * @param funct Funcion a evaluar en formato de string
 * @param puntos Cantidad de puntos en los que se va a dividir el intervalo
 * @param a Inicio del intervalo de integracion
 * @param b Final del intervalo de integracion
 * @return Imprime la aproximacion de la integral junto con su error, ademas devuelve la aproximacion de la integral
*/
ex trapecio_compuesto(string funct, int puntos, double a, double b){
  symbol x;

  vector<ex> s = {};
  double espacio = (b-a)/2;
  double i = a;
  while (i<=b){
    s.push_back(i);
    i = i+espacio;
  }

  double h = s[2]-s[1];
  ex sum = 0;
  i = 0;
  while (i<puntos-1){
    sum = sum + f(funct,soporte[i]) + f(funct,soporte[i+1]);
    i=i+1;
  }

  ex aprox = (h/2)*sum;

  return ex;
}


/**
 * Ejemplo Numérico
 */
int main (int argc, char const* argv[]){
  cout << trapecio_compuesto("1/x", 2) << endl;
  return 0;
}