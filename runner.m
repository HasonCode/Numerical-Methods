#I realize that this is fairly impractical, but I thought it 
#interesting to try out function files and script files for octave
val = bisection(@exponential,-20,20,10^-30,50)
exponential(val)