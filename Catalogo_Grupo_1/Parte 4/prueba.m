function xMax = prueba(soporte)
  syms x;
  n = length(soporte);
  symStr = "1"
  for i=1:n
    charS = num2str(soporte(i))
    symStr = strcat(symStr, "*(x-",charS,")")
  end
  symFMul = sym(symStr)
  fMul = matlabFunction(symFMul)

  solMul = solve(diff(symFMul)==0, x)
  posibleYMax = [fMul(soporte(1)) fMul(soporte(n))]

  for i=1:length(solMul)
    posibleYMax = [posibleYMax fMul(solMul(i))]
  end

  xMax = solve(symFMul==max(posibleYMax),x)

end