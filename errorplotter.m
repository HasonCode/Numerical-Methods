function err = errorplotter(data,root_val)
    iters = data(1:end,7);
    errors = data(1:end,2);
    errors = norm(errors-root_val);
    semilogy(iters,errors);
endfunction