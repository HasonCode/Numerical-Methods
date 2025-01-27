function [x,fx,iters,data] = falseposition(f, a,b,maxiter,tolerance)
    fa = f(a);
    fb = f(b);
    data=[];
    for iters = [1:maxiter]
        x = (b*fa-a*fb)/(fa-fb);
        fx = f(x);
        toadd = [a, x, b, fa, fx, fb, iters];
        data = [data;toadd];
        if (abs(fx)<tolerance)
            return;
        elseif (fx*fa > 0)
            a = x;
            fa = fx;
        else 
            b = x;
            fb = fx;
        endif
    endfor
end
