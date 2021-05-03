function [xs, errorf] = Gauss_Seidel( A, b, xo, tol, imax )

    L = tril(A);
    U = triu(A);
    D = -(A - L - U);
    L = L - D;
    U = U - D;
    x(:, 1) = xo;
    error = zeros(1, imax);
    i = 1;
    check = 0;
    
    
    if abs(inv(D + U)*L) < 1
        
        while check == 0 && i < imax
            i = i + 1;
            x(:, i) = -inv(D + U)*L*x(:,i-1) + inv(D + U)*b;
            error(1, i-1) = abs((sum(x(:,i)) - sum(x(:, i-1)))/sum(x(:,i-1)));
            if error(1, i-1) < tol
                check = 1;
            end
        end
        errorf = error(1,end);
        xs = x(:, i);
        fprintf('x = \n')
        display(xs)
	fprintf('\nerror = %5.8f', error)
        plot(1:i-1,error(1, 2:i), 'marker', 'o', 'linewidth', 1.5)
        xlabel('Iteraciones')
        ylabel('Error')
    else
        fprintf('The Matrix A is not suitable for Gauss - Seidel Iteration method\n')
    end
    
    
end



