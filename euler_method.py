from matplotlib import pyplot as plt
from typing import Union
def integratinator(initial_value:float,step:float, step_count:int, derivative,derivatives:list[float] = None)->list[float]:
    retval = [initial_value]
    if (derivatives!=None):
        if (len(derivatives)!=step_count):
            return []
    for i in range(1,step_count,1):
        if (derivatives==None):
         retval.append(retval[i-1]+derivative(step,retval[-1],i-1))
        else:
           retval.append(retval[i-1]+derivative(step,derivatives,i-1))
    return retval
def velocity_function(time:float,ret_val:float,step_number=0)->float:
    gravity = 9.81
    mass = 90.0
    drag = 0.225
    return (gravity - drag / mass * (ret_val ** 2))*time
def eu_position_function(time, ret_val,step_number):
   return -ret_val[step_number]*time
steps = [0.1,0.5, 1,1.5, 2, 4]
def convergence_grapher(function, step_sizes:list[Union[int,float]], time:float, initial_value:float, xlabel:str, ylabel:str, title:str, numerical_method):
    for i in step_sizes:
        num_steps = int(time//i)
        vals = numerical_method(initial_value,i,num_steps,function)
        processed_vals = []
        for j in range(len(vals)-1):
            processed_vals.append(abs((vals[j+1]-vals[j])/vals[j+1]))
        times = []
        for j in range(1, num_steps):
            times.append(j*i)
        plt.plot(times,processed_vals, marker = ".", label = "Step Size: "+str(i))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.semilogy()
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.clf()
            
def value_grapher(function, step_sizes:list[Union[int,float]], time:float, initial_value:float, xlabel:str, ylabel:str, title:str, numerical_method):
    for i in step_sizes:
        num_steps = int(time//i)
        vals = numerical_method(initial_value,i,num_steps,function)
        times = []
        for j in range(0, num_steps):
            times.append(j*i)
        plt.plot(times,vals, marker = ".", label = "Step Size: "+str(i))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yscale("linear")
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.clf()

convergence_grapher(velocity_function,steps,120,0,"Time (s)", "Convergence", "eulerConvergence",integratinator)

value_grapher(velocity_function,steps,20,0,"Time (s)", "Velocity (m/s)", "eulerValues",integratinator)

time = 160
height = 10000
for i in steps:
    vels = integratinator(0,i,int(time//i),velocity_function)
    pos = integratinator(height,i,int(time//i),eu_position_function,vels)
    times =[]
    for j in range(0,int(time//i)):
        times.append(j*i)
    plt.plot(times,pos,marker = ".", label = f"Step Size: {i}")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.yscale("linear")
plt.legend()
plt.savefig("eulerposition.png")
