import matplotlib.pyplot as plt
from typing import Union
def rungekutta(initial_value:float, step_size:float, num_steps:int, derivative, derivatives:list = None):
    values = [initial_value]
    for i in range(1, num_steps):
        k1,k2,k3,k4 = 0,0,0,0
        if (derivatives==None):
            k1 = derivative(step_size,values[i-1])
            k2 = derivative(step_size*3/2, values[i-1] + step_size*k1/2)
            k3 = derivative(step_size*3/2, values[i-1] + step_size*k2/2)
            k4 = derivative(step_size*2, values[i-1] + step_size*k3)
        else:
            k1 = derivative(step_size,derivatives[i-1])
            k2 = derivative(step_size*3/2, derivatives[i-1] + step_size*k1/2)
            k3 = derivative(step_size*3/2, derivatives[i-1] + step_size*k2/2)
            k4 = derivative(step_size*2, derivatives[i-1] + step_size*k3)
        values.append(values[i-1] + step_size/6*(k1 + 2*k2 + 2*k3 + k4))
    return values

def velocity_function(time:float,ret_val:float,step_size = 0)->float:
    gravity = 9.81
    mass = 90.0
    drag = 0.225
    return (gravity - drag / mass * (ret_val ** 2))*time

def position_function(time, ret_val, step_size = 0):
   return -ret_val*time

step_sizes = [ 0.1,0.5,1, 1.5, 2]
def convergence_grapher(function, step_sizes:list[Union[int,float]], time:float, initial_value:float, xlabel:str, ylabel:str, title:str, numerical_method, other_derivative = None, second_init = None):
    for i in step_sizes:
        num_steps = int(time//i)
        vals = numerical_method(initial_value,i,num_steps,function)
        processed_vals = []
        times = []
        if other_derivative == None:
            for j in range(len(vals)-1):
                processed_vals.append(abs((vals[j+1]-vals[j])/vals[j+1]))
            for j in range(1, num_steps):
                times.append(j*i)
        else:
            vals = numerical_method(second_init,i,num_steps,other_derivative,vals)
            for j in range(len(vals)-1):
                processed_vals.append(abs((vals[j+1]-vals[j])/vals[j+1]))
            for j in range(1, num_steps):
                times.append(j*i)
        plt.plot(times,processed_vals, marker = ".", label = "Step Size: "+str(i))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.semilogy()
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.clf()
            
def value_grapher(function, step_sizes:list[Union[int,float]], time:float, initial_value:float, xlabel:str, ylabel:str, title:str, numerical_method, other_derivative = None, second_init = None):
    for i in step_sizes:
        num_steps = int(time//i)
        vals = numerical_method(initial_value,i,num_steps,function)
        times = []
        for j in range(0, num_steps):
            times.append(j*i)
        if other_derivative != None:
            vals = numerical_method(second_init,i,num_steps,other_derivative,vals)
        plt.plot(times,vals, marker = ".", label = "Step Size: "+str(i))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yscale("linear")
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.clf()
# vals = rungekutta(0,0.5,100,velocity_function)
convergence_grapher(velocity_function,step_sizes,80,0,"Time (s)","Convergence","RK4Convergence", rungekutta)
value_grapher(velocity_function,step_sizes,80,0,"Time (s)","Velocity (m/s)","RK4Values", rungekutta)
step_sizes = [ 0.1,0.3,0.5,1]

value_grapher(velocity_function,step_sizes,217,0,"Time (s)","Position (m)","RK4Positions", rungekutta,position_function,10000)

from euler_method import integratinator

plt.clf()

step_sizes = [0.5,1, 2]
time = 160
for i in step_sizes:
    num_steps = int(time//i)
    vals1 = rungekutta(0,i,num_steps,velocity_function)
    vals2 = integratinator(0,i,num_steps,velocity_function,None)
    times = []
    for j in range(1,num_steps):
        times.append(i*j)
    processed_vals1, processed_vals2 = [],[]
    for j in range(num_steps-1):
        processed_vals1.append(abs((vals1[j+1]-vals1[j])/vals1[j+1]))
        processed_vals2.append(abs((vals2[j+1]-vals2[j])/vals2[j+1]))
    plt.plot(times, processed_vals1, marker = ".", label =f"RK4 Step Size: {i}")
    plt.plot(times, processed_vals2, marker = ".", label =f"Euler Step Size: {i}")
plt.semilogy()
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Convergence")
plt.savefig("convergenceComp.png")