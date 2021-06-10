
function euler()
  pkg load symbolic;
  warning('off','all');
  clc;
  
  
  f='y-x^2+1';
  y0=0.5;
  a=0;b=2;
  n=11;
  [xv,yv,p]=metodo_euler(f,a,b,y0,n)
  
  %Graficacion del polinomio de interpolacion y los puntos (xv,yv)
  stem(xv,yv,'LineStyle','none');
  hold on 
  ezplot(p,[a,b]);


end



% Funcion auxiliar que aproxima una solucion al problema de Cauchy haciendo uso del metodo de Euler
% Entradas : 
%      f: Funcion f(x,y).
%      a: Limite inferior del intervalo.
%      b: Limite superior del intervalo.
%      y0: Valor inicial de y para la aproximacion.
%      n: Numero de puntos con los que se quiere realizar la aproximacion
% Salida : 
%      xv : Valores de los puntos en X.
%      yv : Valores de los puntos en Y.
%      p  : Polinomio de interpolacion 

function[xv,yv,p]= metodo_euler(f,a,b,y0,n)
  syms x y;
  f1=matlabFunction(sym(f));
  
  %Calculo de la constante h
  h=(b-a)/(n-1);
  
  %Calculo de los valores de x
  xv=a:h:b;
  
  %Calculo de los valores de y
  yv=zeros(1,n);
  yv(1)=y0;
  for k=1:n-1
    yv(k+1)=yv(k)+h*f1(xv(k),yv(k));
  endfor
  
  %Calculo del polinomio de interpolacion
  p=ddnewton(xv,yv);
  return
  
end 


%Funcion que implementa el metodo de las diferencias divididas de Newton para el calculo del polinomio de interpolacion formado por los puntos (xv,yv)
function p=ddnewton(xv,y)
  syms x;
  m=length(xv);
  n=m;
  fs=[];
  for i=1:n
    f=zeros(1,m);
    for j=1:n
      if i==1
        f(j)=y(j);
        
      else
        f(j)=((fs(i-1,j+1)-fs(i-1,j))/(xv(i+j-1)-xv(j)));
      endif
    endfor
  fs=[fs;f]; 
  n-=1;  
  endfor
  
  p=0;
  
  for i=1:m
    if i==1
      p+=fs(i,1);
    else
      c=1;
      for j=1:i-1
        c*=(x-xv(j));
      endfor
      p+=fs(i,1)*c;
    endif
  endfor

  return;
 
 
end