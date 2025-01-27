function val = exponential(x)
    val = exp(-x.^3-cos(x))-sin(x)./x;
end