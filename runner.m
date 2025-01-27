#I realize that this is fairly impractical, but I thought it 
#interesting to try out function files and script files for octave
[x,fx,iter,data]= bisection(@test_function,-2,7,50,eps);
errorplotter(data,27^(1/2))