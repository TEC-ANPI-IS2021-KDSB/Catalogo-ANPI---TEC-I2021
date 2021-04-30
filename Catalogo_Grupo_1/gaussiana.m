% Resuelve el sistema de ecuaciones Ax=B
% Entradas: A: Matriz de coeficientes
%           B: Matriz de términos independientes
% Salidas:  X: Matriz resultante 
function [X] = gaussiana(A, B) 
  n = length(A);
  X=zeros(1,n);
  Ab=[A transpose(B)]

  for k=1:n-1
    for i=k+1:n
      mik = Ab(i,k)/Ab(k,k)
      for j=k:n+1
        Ab(i,j)=Ab(i,j)-mik*Ab(k,j);
      end
    end
  end
  X=sust_atras(Ab(:,1:n),B);
end

function [X] = sust_atras(A, B)
  n = length(A);
  X=zeros(1,n);
  for i=n:-1:1
    sum = 0;
    for j=i+1:n
      sum = sum + A(i,j)*X(j);
    end
    X(i) = (1/(A(i,i)))*(B(i)-sum);
  end
end

