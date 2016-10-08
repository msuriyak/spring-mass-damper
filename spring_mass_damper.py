################ Project 1 SDES (AE663) ################

import math

################ Implementation of RK4 ################
def rk4(f, x0, t0, t1, n, param = []):
    '''
    Solve the IVP 
        dot(x) = f(x, t, param) 
    Initial conditions:
        x(t0) = x0
    from t0 to t1 (n steps)    
    '''
    import numpy as np
    if type(x0) is list:
        vx = np.array([np.array([float(0)]*len(x0))]*(n+1))
    else:
        vx = np.array([float(0)]*(n+1))   

    time = [0]*(n+1)
    vx[0] = x0
    x = x0
    time[0] = t0
    t = t0
    
    h = (t1 - t0)/float(n)
    for i in range(1,n+1):
        k1 = h*np.array(f(x, t, param))
        k2 = h*np.array(f(x + 0.5*k1, t + 0.5*h, param))
        k3 = h*np.array(f(x + 0.5*k2, t + 0.5*h, param))
        k4 = h*np.array(f(x + k3, t + h, param))
        vx[i] = x + (1.0/6)*(k1 + 2*k2 + 2*k3 + k4)
        time[i] = t0 + i*h 
        t = time[i]
        x = vx[i]
    if type(x0) is list:
        res_vx = [list(k) for k in vx]
    else:
        res_vx = [k for k in vx]
    return res_vx, time

################ Testing RK4 ################

def check_rk4_1(y, t, param = []):
    '''
    Solving differential equation 
        dot(y) = y ; 
        y(0) = 1, t0 = 0, t = 5, n = 1000   
    '''
    return y

def check_rk4_2(y, t, param = []):
    '''
    Solving differential equation 
        dot(y1) = y1 + y2, dot(y2) = y1 - y2; 
        y(0) = [10, 5], t0 = 0, t = 5, n = 1000   
    '''
    return [y[1], y[0]]

def check_rk4_3(y, t, param = []):
    '''
    Solving differential equation 
        dot(y1) = y1 , dot(y2) = - y2; 
        y(0) = [1, 1], t0 = 0, t = 5, n = 1000   
    '''
    return [y[0] , -y[1]]

def check_rk4_4(y, t, param = []):
    '''
    Solving differential equation 
        dot(y1) = y1 , dot(y2) = - y2; 
        y(0) = [1, 1], t0 = 0, t = 5, n = 1000   
    '''
    return [-y[1] , y[0]]


def run_rk4_on_check_rk4_1():
    y0 = 1
    t0 = 0
    t1 = 5
    n = 1000
    y,t = rk4(check_rk4_1, y0, t0, t1, n)
    return ( max( [ abs((y[i] - math.exp(t[i]))) for i in range(n+1) ] ) )
    
def run_rk4_on_check_rk4_2():
    y0 = [2, 0]
    t0 = 0
    t1 = 5
    n = 1000
    y,t = rk4(check_rk4_2, y0, t0, t1, n)
    return ( max( [ abs((y[i][0] - math.exp(t[i]) - math.exp(-t[i]) )) for i in range(n+1) ] ), \
           max( [ abs((y[i][1] - math.exp(t[i]) + math.exp(-t[i]) )) for i in range(n+1) ] )  ) 

def run_rk4_on_check_rk4_3():
    y0 = [1, 1]
    t0 = 0
    t1 = 5
    n = 1000
    y,t = rk4(check_rk4_3, y0, t0, t1, n)
    return ( max( [ abs((y[i][0] - math.exp(t[i]))) for i in range(n+1) ] ), \
           max( [ abs((y[i][1] - math.exp(-t[i]))) for i in range(n+1) ] )  )    

def run_rk4_on_check_rk4_4():
    y0 = [1, -1]
    t0 = 0
    t1 = 5
    n = 1000
    y,t = rk4(check_rk4_4, y0, t0, t1, n)
    return ( max( [ abs((y[i][0] - math.sin(t[i]) - math.cos(t[i]) )) for i in range(n+1) ] ), \
           max( [ abs((y[i][1] - math.sin(t[i]) + math.cos(t[i]) )) for i in range(n+1) ] )  ) 
    
def test_rk4():
    tol = 10**-5
    
    res = run_rk4_on_check_rk4_1()
    assert res < tol
    
    res = run_rk4_on_check_rk4_2()
    assert res[0] < tol and res[1] < tol

    res = run_rk4_on_check_rk4_3()
    assert res[0] < tol and res[1] < tol

    res = run_rk4_on_check_rk4_4()
    assert res[0] < tol and res[1] < tol


################ Plotting Options ################

def plot(x, y, Title, xTitle, legend,option = False, show = True):
    '''
    Plots the values with linespecs set 
    '''
    import matplotlib.pyplot as plt
    
    plt.figure()
    pos, = plt.plot(x, y[0], '-ro', lw=1, label=legend[0])
    vel, = plt.plot(x, y[1], '-bx', lw=1, label=legend[1])
    plt.hold('on')
    plt.xlabel(xTitle, family='sans-serif', style='italic',size=10)
    plt.title(Title, family='sans-serif', style='italic',size=10)
    plt.legend(handles=[pos, vel], fontsize=10)
    if(option):
        plt.savefig(Title + '.png') 
    if(show):
        plt.show()
    


################ Mass-spring damper dynamics ################

def read_parameters(path):
    parameters = open(path,'rt')
    parameters = parameters.readlines()
    parameters = parameters[0].rstrip()
    parameters = parameters.split(',')
    parameters = [float(n) for n in parameters]
    return parameters

def dynamics(state, t, param = []):
    m = param[0]
    c = param[1]
    k = param[2]
    force = param[3]
    if force is not None:
        f = force(state,t)
    else:
        f = 0  
    zeta = c/(2*(k*m)**0.5)
    omega_o = (k/m)**0.5
    state_dot = [state[1], -2*zeta*omega_o*state[1] - state[0]*omega_o**2 + f/m]
    return state_dot

def force(state, t):
    return 4*math.sin(0.5*t)    

if __name__ == '__main__':
    pass