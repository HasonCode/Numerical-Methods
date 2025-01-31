function var = processedexponential(x)
    var = exp(-x.^3-cos(x))-sin(x)./x + x;
end