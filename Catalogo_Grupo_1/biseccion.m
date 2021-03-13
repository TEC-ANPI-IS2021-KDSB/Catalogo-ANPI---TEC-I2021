%function file, save as biseccion.m
% Para ejecutarla en la ventana de comandos usar:
%1) biseccion
%2) f=@(x)x-2; Donde la funcion a estudiar se cambia
%3) [a,e] = biseccion(f,[4,7],10,1e-6) Donde estos parametros cambian
function [a,e] = biseccion(funcion,intervalo,IteracionesMaximas,tolerancia)
elemento_n=0;
error=1/tolerancia;
intervalo(1);
intervalo(2);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
while error(end)>tolerancia && elemento_n<IteracionesMaximas
elemento_n=elemento_n+1;
a=(intervalo(1)+intervalo(2))/2;
if funcion(intervalo(1))*funcion(a)<0
intervalo(2)=a;
else
intervalo(1)=a;
end
error(elemento_n)=abs(intervalo(1)-intervalo(2));
end
e=error(end);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Graficacion
plot(1:elemento_n,error,'--o')
xlabel('Cantidad Iteraciones')
ylabel('Error |f(Xk)|')
title('Gráfico Iteraciones vs Errores')

