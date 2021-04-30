clc;clear;

A=[1 2 4; 2 -1 1; 1 0 1]
alpha=max(eig(A*A'))
X=(1/alpha)*A';
I=eye(3);
for k=1:15
  -(A*X)
  X=X*(2*I-A*X);
  error = norm(A*X*A-A,'fro');
end