#include<ginac/ginac.h>

using namespace std;

using namespace GiNaC;


ex Lagrange( vector<double> xx, vector<double> yy, int k, symbol x){
	ex Lk = 1;
	int n = min(xx.size(),yy.size());
	for(int i = 0; i<n; i++){
		if(i == k) continue;
		Lk*= (x-xx[i])/(xx[k]-xx[i]);
	}
	return Lk;
}
ex Lagrange(vector<double> xx, vector<double> yy,symbol x){
	ex polLagrange = 0;
	int n = min(xx.size(),yy.size());
	for(int i = 0; i<n; i++){
		polLagrange+= yy[i]*Lagrange(xx,yy,i,x);
	}
	return polLagrange.simplify_indexed();	
}

int main(){
	vector<double> xx = {1.0,2.0,3.0,4.0};
	vector<double> yy = {2.0,3.0,5.0,8.0};
	symbol x("x");
	cout<<Lagrange(xx,yy,x)<<"\n";
	
	
	
}
