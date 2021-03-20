clc clear
pkg load symbolic

function var_vector = read_var (var)
  x = [];
  rem = strtrim(var);
  do
    [tok, rem] = strtok(rem);
    x = [x sym(tok)];
  until (isempty(rem))
  var_vector = x ;
endfunction

function min = descenso_coordinadof (f, var, x_0, iterMax, tol)
  x_var = read_var (var)
  x_k = x_0;
  fs = sym(f); %Convierte el texto a simbolico
  #  f=matlabFunction(f1); %Función f en formato del lenguaje M
  for k=1:iterMax
    [~, n] = size(x_var);
    x_j = sym();
    for j=1:n
      x_j(1:n) = x_k(1:n);
      x_j(j) = x_var(j);
      x_k(j) = fminsearch (matlabFunction(subs(fs, x_var, x_j)), x_k(j));
    endfor
  endfor
  min = x_k
endfunction

descenso_coordinadof("(x-2)^2+(y+3)^2+y*x", 'x y', [1 1], 9, 1)