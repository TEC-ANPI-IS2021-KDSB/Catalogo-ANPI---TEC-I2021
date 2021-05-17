function xMax = prueba(soporte)
  syms x;
  n = length(soporte);
  symStr = "1";
  for i=1:n
    charS = num2str(soporte(i));
    symStr = strcat(symStr, "*(x-",charS,")");
  end
  symFMul = sym(symStr);
  fMul = matlabFunction(symFMul);

  [fmax, xMax] = calcXMax(soporte(1),soporte(n), symFMul)
end

function [fmax, x_max] = calcXLim(a,b,f)
  pkg load symbolic;
  syms x;
  f1=matlabFunction(f);
  fd = diff(f,x)==0;
  puntos_criticos = double(solve(fd,x))';
  puntos_a_evaluar=[a b puntos_criticos]
  valores_evaluados= [abs(f1(puntos_a_evaluar))];
  [fmax,i_max]=max(valores_evaluados);
  x_max = puntos_a_evaluar(i_max);
end