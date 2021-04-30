
#include <iostream>
#include <armadillo>

using namespace arma;

Mat<double> pseudoinversa(Mat<double> A, Mat<double> B, int iterMax, double tol){
  int n = A.n_rows;
  int m = A.n_cols;

  double alpha = eig_sym(A*trans(A)).max();
  cout << alpha<<endl;
  
  Mat<double> X, Xo, Xkm1;
  X = (1/alpha)*trans(A);
  Mat <double> I(n,m, fill::eye);

  cout << I << endl;

  int k=0;

  while(k<iterMax){
    cout <<  -(A*X) << endl;
    X=X*(2*I-A*X);

    if(norm((A*X*A)-A)<tol){
      break;
    }

    k=k+1;
  }

  return X;
}

int main(void){
  Mat<double> A = {{1,2,4},{2,-1,1},{1,0,1}};
  Mat<double> B = {4,3,9};
  cout << pseudoinversa(A,B,200, 0.0000000001)<<endl;;

  return 0;
}
