function root = bisection(f, a,b,err)
    root = (a+b)/2;
    while ((f((a+b)/2)<err))
        if (f(root)*f(a) > 0)
            a = root ;
        else 
            b = root;
        endif
        root = (a+b)/2;
    end
end
