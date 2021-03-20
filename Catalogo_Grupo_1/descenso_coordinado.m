clc clear
pkg load symbolic
warning('off','all');

% Funcion que aproxima el mínimo de una funcion matematica de multiples variables
% mediante el metodo de descenso coordinado
% Entradas : 
%            f : funciona a minimizar en formato de texto 
%            var : variables usadas en la funcion f en formato de texto. Ej "x y z"
%            x_0 : valores iniciales de los parametros de entrada. Ej [1 1 1]
%            iterMax : numero maximo de iteraciones
%            tol : tolerancia para la norma del gradiente de la funcion en la aproximacion
% Salidas : 
%            aproximacion : aproximacion al minimo de f
%            error : norma del gradiente de la funcion en la aproximacion

function [aproximacion, error] = descenso_coordinadof (f, var, x_0, iterMax, tol)
  x_var = read_var (var); % Se convierten las variables en simbolico
  x_k = x_0;  % Array de aproximaciones en los parametros
  fs = sym(f); % Convierte el texto a simbolico
  gs = gradient(fs); % Gradiente de f
  error = [];
  for k=1:iterMax
    [~, n] = size(x_var);
    for j=1:n % Se aplica el metodo de Gauss-Seidel:
      % Se substituyen todas las variables menos la j-esima:
      f_xj = subs(fs, x_var(1:end~=j), x_k(1:end~=j)); 
      % Se encuentra el argmin de la funcion anterior
      x_k(j) = fminsearch (matlabFunction(f_xj), x_k(j));
    endfor
    % Se calcula la norma
    norm_grad = norm(double(subs(gs, x_var, x_k)));
    error= [error norm_grad];
    if norm_grad < tol
      break;
    end
  endfor
  % Se grafica
  plot(1:k,error,'--o')
  xlabel('Cantidad Iteraciones')
  ylabel('Error')
  title('Gráfico Iteraciones vs Errores')
  
  aproximacion = double(subs(fs, x_var, x_k)); 
  error= norm_grad;
endfunction

% Funcion auxiliar para convertir el texto de las variables en symbolicos
function var_vector = read_var (var)
  % Se extraen los tokens separados por espacios y se agregan a un array
  % de symbolics
  x = [];
  rem = strtrim(var);
  do
    [tok, rem] = strtok(rem);
    x = [x sym(tok)];
  until (isempty(rem))
  var_vector = x ;
endfunction

%Ejemplo Numerico
[aproximacion error] = descenso_coordinadof("(x-2)^2+(y+3)^2+(x+y+z)^2", 'x y z', [1 1 1], 15, 1e-3)