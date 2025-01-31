function [x, fx, iters,data] = secantmethod(a,b,f,maxiter,tolerance)
    arr = [a,b];
    fa = f(a);
    fb = f(b);
    next_val = (fb*arr(end-1)-arr(end)*fa)/(fb-fa);
    data = [[a,fa,b,fb,next_val,0]];
    for iters = [1:maxiter]
        arr = [arr,next_val];
        fa = f(arr(end-1));
        fb = f(arr(end));
        next_val = (fb*arr(end-1)-arr(end)*fa)/(fb-fa);
        to_add = [arr(end-1),fa,arr(end),fb,next_val,iters];
        data = [data;to_add];
        if abs(arr(end)-arr(end-1))<tolerance
            x = arr(end);
            fx = f(x);
            return;
        endif
    endfor
    x = arr(end);
    fx = f(x);
end