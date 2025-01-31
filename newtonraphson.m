function [x, fx, iters,data] = newtonraphson(a,f,df,maxiter,tolerance)
    fa = f(a(end));
    dfa = df(a(end));
    data =[[a(end),fa,dfa,0]];
    for iters = [1:maxiter]
        a = [a,a(end)-fa/dfa];
        fa = f(a(end));
        dfa=df(a(end));
        to_add = [a(end),fa,dfa,iters];
        data = [data;to_add];
        if abs(a(end)-a(end-1))<tolerance
            x = a(end);
            fx = f(x);
            return;
        endif
    endfor
    x = a(end);
    fx = f(x);
end