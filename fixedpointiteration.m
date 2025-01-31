function [x,fx,iters,data] = fixedpointiteration(a,f,maxiter,tolerance)
    fa = f(a(end));
    data = [[a(end),fa,0]];
    for iters = [1:maxiter]
        a = [a,f(a(end))];
        fa = f(a(end));
        to_add = [a(end),fa,iters];
        data = [data;to_add];
        if abs(a(end)-a(end-1))<tolerance
                x = a(end);
                fx = f(a);
            return;
        endif
    endfor
    x = a(end);
    fx = f(a);
endfunction