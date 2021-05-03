#include <iostream>
#include <vector>
#include <cmath>
using namespace std;



vector<vector<double> > cholesky(double **A, int n){

	// Inicializacion de la matriz decompuesta, como un vector de vectores
	// El objeto esta lleno de ceros
	vector<vector<double> > L(n, vector<double>(n, 0));

    double sum1 = 0.0, sum2 = 0.0;
    L[0][0] = sqrt(A[0][0]);

    for (int i = 0; i < n; i++){
    	L[i][0] = A[i][0]/L[0][0];
	}


    for (int i = 1; i < n; i++){

        for (int k = 0; k <= i - 1; k++){
            sum1 += pow(L[i][k], 2.0);
        }

        L[i][i] = sqrt(A[i][i] - sum1);

        for (int j = i + 1; j < n; j++){
            for (int k = 0; k <= i - 1; k++){
                sum2 += L[j][k]*L[i][k];
            }

            L[j][i] = 1.0/L[i][i]*(A[j][i] - sum2);
            sum2 = 0;
        }

        sum1 = 0;
    }

    return L;
}

// Esta funcion devuelve la matriz transpuesta de una matriz dada
vector<vector<double> > transpose(vector<vector<double> > A, int n){

	vector<vector<double> > T(n, vector<double>(n, 0));

	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			T[i][j] = A[j][i];
		}
	}
	return T;
}

vector<double> fact_cholesky(double **A, double *b, int n){

	// Vector of vectors (double)
	vector<vector<double> > L(n, vector<double>(n, 0));
	vector<vector<double> > Lt(n, vector<double>(n, 0));
	L = cholesky(A, n);
    Lt = transpose(L, n);

	vector<double> x(n, 0);
	vector<double> z(n, 0);

	double sum1, sum2;

	// Sustitucion hacia adelante
	z[0] = b[0]/L[0][0];
	for (int i = 1; i < n; i++){
		sum1 = 0.0;
		for (int j = 0; j < i; j++){
			sum1 += L[i][j]*z[j];
		}

		z[i] = (b[i] - sum1)/L[i][i];
	}

	for (int i = 0; i < n; i++){
    	cout << "y[" << i << "] = " << z[i] << "\n";
    }
	cout << "\n";
	// Sustitucion hacia atras

	x[n-1] = z[n-1]/Lt[n-1][n-1];
	for (int i = n - 2; i > -1; i--){
		sum2 = 0.0;
		for (int j = i + 1; j < n; j++){
			sum2 += Lt[i][j]*x[j];
		}
		x[i] = (z[i] - sum2)/Lt[i][i];

	}

	return x;


}

int main(){

	// n: Tama�o de la matriz (simetrica)
	int n = 4;
	// A: Matriz a ser descompuesta por la Descomposicion de Choleski
    double A[][4] = {{25,15,-5,-10}, {15, 10, 1, -7}, {-5, 1, 21, 4}, {-10, -7, 4, 18}};
    // b: Vector de valores independientes del sistema de ecuaciones lineales A�x = b
    double b[] = {-25, -19, -21, -5};

	/* La funcion choleski() y la funcion solve_chol()
	reciben como argumento la matriz de coeficientes en forma de un puntero de punteros
	debido a esto, no se puede pasar a esta los arrays A[][n]. El vector de coeficientes
	independientes b se recibe de igual forma

	Para esto, se inicializan los punteros de punteros A1 y b1 en las siguientes lineas,
	esta es una forma de crear arrays dinamicos
	*/

    double **A1 = NULL;
    double *b1 = NULL;
    A1 = new double *[n];
    b1 = new double [n];
    for(int i = 0; i < n; i++){
    	A1[i] = new double [n];
	}

    for(int i = 0; i < n; i++){
    	b1[i] = b[i];
    	for (int j = 0; j < n; j++){
    		A1[i][j] = A[i][j];
		}
	}

    // Vector de vectores (double) que representa una matriz
	vector<vector<double> > L(n, vector<double>(n, 0));
	// CLlamada a la funcion que descompone la matriz dada seg�n la descomposicion de Choleski
    L = cholesky(A1, n);

	// Se imprime en pantalla la matriz descompuesta
    for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			cout << "L[" << i << "][" << j << "] = " << L[i][j] << "\t";
		}
		cout << "\n";
	}

	cout << "\n";

    // Solucion del sistema lineal A�x = b
    vector<double> u(n, 0);
    u = fact_cholesky(A1, b1, n);

	// Se imprime en pantalla la solucion del sistema lineal A�x = b
    for (int i = 0; i < n; i++){
    	cout << "x[" << i << "] = " << u[i] << "\n";
    }

    cout << "\nPrograma terminado con exito :D\n";

    return 0;

}
