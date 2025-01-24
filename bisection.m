function root = bisection(f, a,b,err,num_iter)
    root = (a+b)/2.0;
    for count = [1:num_iter]
        if (abs(f(root))<err)
            return;
        elseif (f(root)*f(a) > 0)
            a = root;
        else 
            b = root;
        endif
        root = (a+b)/2.0;
    endfor
end
