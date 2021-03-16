function muller
   f='sin(x) - x / 2';
   x0=2;
   x1=2.2;
   x2=1.8;
   iterMax=100;
   tol=10^-68;
   [rx,error]=mullerAux(f,x0,x1,x2,tol,iterMax)
end

function[rx,error]=mullerAux(f,x0,x1,x2,tol,iterMax)
  pkg load symbolic
  syms x;
  f1=sym(f);
  f=matlabFunction(f1);
  rx=0;
  e=[];
  for i=1:iterMax
    
    a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) * (f(x1) - f(x2))) / ((x0 - x1) * (x0 - x2) * (x1 - x2));
    b = (((x0 - x2) ** 2) * (f(x1) - f(x2)) - ((x1 - x2) ** 2) * (f(x0) - f(x2))) / ((x0 - x1) * (x0 - x2) * (x1 - x2));
    c = f(x2);
    
    rx=x2 - ((2 * c) / (b + (b / abs(b)) * sqrt(b ** 2 - 4 * a * c)));
    error=abs(f(rx));
    e=[e error];
    if error<tol
      break
    endif
    rx0=abs(rx-x0);
    rx2=abs(rx-x2);
    
    if rx0<rx2
      x2=x1;
      x1=rx;
    else
      x0=x1;
      x1=rx;
    endif
  endfor
  plot(e)
  display(["Aproximacion: ",num2str(rx)]);
  display(["Iteraciones:",num2str(i)]);
  display(["Error relativo Normalizado:",num2str(error)]);

end