#include<ginac/ginac.h>

using namespace std;

using namespace GiNaC;


ex Lagrange( vector<double> xx, int k, symbol x){
	/* Entradas:
	 * xx: vector de puntos en x
	 * x : Variable sobre la queremos el polinomio de Lagrange
	 * Salida:
	 * Polinomio simbólico en variable x, que tiene el polinomio Lk(x) que cumple que 
	 * Lk(xx[i]) = 1 si i == k y 0 sino 
	 */
	ex Lk = 1;
	int n = min(xx.size(),yy.size());
	for(int i = 0; i<n; i++){
		if(i == k) continue;
		Lk*= (x-xx[i])/(xx[k]-xx[i]);
	}
	return Lk;
}
ex Lagrange(vector<double> xx, vector<double> yy,symbol x){
	/* Entradas:
	 * xx: vector de puntos en x
	 * yy: vector de puntos en y
	 * x : Variable sobre la queremos el polinomio de Lagrange
	 * Salida:
	 * Polinomio simbólico en variable x, que tiene el polinomio de
	 * lagrange L(x) que cumple que L(xx[i]) = yy[i]
	 */
	ex polLagrange = 0;
	int n = min(xx.size(),yy.size());
	for(int i = 0; i<n; i++){
		//Agregamos cada termino de la sumatoria al polinomio de Lagrange 
		polLagrange+= yy[i]*Lagrange(xx,yy,i,x);
	}
	//Devolvemos el polinomio simplificado
	return polLagrange.simplify_indexed();	
}

int main(){
	
	vector<double> xx = {1.0,2.0,3.0,4.0};
	vector<double> yy = {2.0,3.0,5.0,8.0};
	symbol x("x");
	cout<<Lagrange(xx,yy,x)<<"\n";
	
	
	
}
