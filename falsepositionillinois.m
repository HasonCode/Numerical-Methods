function [x,fx,iters,data] = falsepositionillinois(f, a,b,maxiter,tolerance)
    fa = f(a);
    fb = f(b);
    signval = 0
    data=[];
    for iters = [1:maxiter]
        x = (b*fa-a*fb)/(fa-fb);
        fx = f(x);
        toadd = [a, x, b, fa, fx, fb, iters];
        data = [data;toadd];
        if (abs(fx)<tolerance)
            return;
        elseif (fx*fa > 0)
            if signval == 1
                fa=fa*0.5;
            endif
            a = x;
            fa = fx;
            signval = 1;
        else 
            if signval==-1
                fb=fb*0.5
            endif
            b = x;
            fb = fx;
            signval = -1
        endif
    endfor
end
