''
clc clear

% Funcion que aproxima el valor propio de mayor magnitud de una matriz
% y su respectivo vector propio mediante el metodo qr
% Entradas : 
%      A : matriz en la cual realizar los calculos
% Salidas : 
%      valor: valor propio de mayor magnitud
%      vector : vector propio del valor de mayor magnitud
function [valor, vector] = metodo_qr_f(A)
  # Se inicializan algunos valores auxiliares
  [n, ~] = size(A);
  valores_ind = sub2ind([n,n], [1:n], [1:n]);
  errores = 0;
  
  # Se realiza el metodo iterativo
  U = eye(n);
  An = A;
  for i =1:100
    [Q R] = qr(An);
    An = R * Q;
    U = U*Q;   
    
    # Se calcula el error absoluto 
    # Para esto se encuentra el valor propio de mayor magnitud y
    # se realiza la operacion A*v - lambda*v que da el error
    
    # Se encuentra el indice del maximo 
    valores = An(valores_ind); 
    [~, max_ind] = max(abs(valores));
    # Se define el valor y vector propios aproximados
    valor = An(max_ind);
    vector = U(:,max_ind);
    # Se calcula el error
    errores(i) = norm(A*vector - valor*vector);
    if(errores(i) < 10e-8)
      break
    end
  end
 
  # Se muestra el gráfico de error
  
  plot(1:i,errores,'--o')
  xlabel('Cantidad Iteraciones')
  ylabel('Error')
  title('Grafico Iteraciones vs Error')
  
endfunction

# Funcion de prueba
[valores, vectores] = metodo_qr_f([0 11 -5; -2 17 -7; -4 26 -10])