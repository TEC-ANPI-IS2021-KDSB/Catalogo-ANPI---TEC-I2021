#include <iostream>
#include <armadillo>
#include "matplotlibcpp.h"
using namespace std;
using namespace arma;
namespace plt = matplotlibcpp;
/**
 * Funcion para calcular la solucion de un sistema de ecuaciones
 * mediante el metodo de jacobi
 * @param A Matriz cuadrada de armadillo
 * @param b Vector de terminos independientes de armadillo
 * @param x0 Solucion inicial
 * @param tol Tolerancia
 * @param iterMax Cantidad maxima de iteraciones
 * @return <x, error> Tupla del vector de solucion y el error de la aproximacion
 */
tuple<vec, double> jacobi(mat A, vec b, vec x0, double tol, int iterMax){
    mat L(size(A), fill::zeros);
    mat D(size(A), fill::zeros);
    mat U(size(A), fill::zeros);
    //Se separa A en L , D , U
    for(int i = 0; i< A.n_rows; i++){
        for(int j = 0; j< A.n_cols; j++){
            if(i>j){
                U(i,j) = A(i,j);
            }else if(i<j){
                L(i,j) = A(i,j);
            }else{
                D(i,j) = A(i,j);
            }
        }
    }

    // Se realiza el metodo iterativo
    mat T = - D.i()*(L+U);
    mat c = D.i()*b;
    vector<double> graphX(iterMax), graphY(iterMax);

    int i = 0;
    vec x = std::move(x0);
    double error;
    do{
        x = T*x + c;
        i++;
        error = norm(A*x-b);
        graphX.insert(graphX.begin(),i);
        graphY.insert(graphY.begin(), error);
    }while  (error> tol && i<iterMax);

    //Se grafica
    graphX.resize(i);
    graphY.resize(i);
    plt::plot(graphX,graphY);
    plt::suptitle("Error en el Método de Jacobi");
    plt::xlabel("Iteraciones");
    plt::ylabel("Error");
    plt::show();

    // Se retorna el resultado
    return make_tuple(x, error);
}
/**
 * Ejemplo Numerico
 */
int main(int argc, char const *argv[])
{
    mat A("5 1 1; 1 5 1; 1 1 5");
    vec b("7 7 7");
    vec x0("0 0 0");

    tuple<vec, double> result  = jacobi(A, b, x0, 1e-8, 50);

    // Se imprime el resultado

    vec x = get<0>(result);
    cout.precision(15);
    cout.setf(ios::fixed);
    x.raw_print("X: ");

    double error = get<1>(result);
    cout<< "Error: ";
    cout<< error <<endl;

    return 0;
}
