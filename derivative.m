% exp(-x.^3-cos(x))-sin(x)./x
function val = derivative(x)
    val = -3*x.^2+sin(x)*exp(-x.^3-cos(x))-(x*cos(x)-sin(x))./(x.^2);
end