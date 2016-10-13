import spring_mass_damper as smd
import math

################ Plots for the tex file ################

def plot_underdamped():
    m,c,k = [1, 2, 4]
    
    # free response
    y, t = smd.rk4(smd.dynamics, [10,5], 0, 5, 35, [m, c, k, None])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time $(m=1, c=2, k=4)$', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Free_response_underdamped', False)

    # forced response
    # under natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_underdamped_under', False)
    # above natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(4*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(4t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_underdamped_over', False)
    # at natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(2*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(2t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_underdamped_natural', False)

def plot_critically_damped():
    m,c,k = [1, 4, 4]
    
    # free response
    y, t = smd.rk4(smd.dynamics, [10,5], 0, 20, 150, [m, c, k, None])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time $(m=1, c=2, k=4)$', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Free_response_criticaldamped', False)

    # forced response
    # under natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_criticaldamped_under', False)
    # above natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(4*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(4t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_criticaldamped_over', False)
    # at natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(2*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(2t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_criticaldamped_natural', False)

def plot_overdamped():
    m,c,k = [1, 8, 4]
    
    # free response
    y, t = smd.rk4(smd.dynamics, [10,5], 0, 20, 150, [m, c, k, None])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time $(m=1, c=2, k=4)$', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Free_response_overdamped', False)

    # forced response
    # under natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_overdamped_under', False)
    # above natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(4*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(4t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_overdamped_over', False)
    # at natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(2*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(2t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_overdamped_natural', False)

def plot_special_case():
    m,c,k = [1, 0, 4]
    
    # free response
    y, t = smd.rk4(smd.dynamics, [10,5], 0, 20, 150, [m, c, k, None])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time $(m=1, c=2, k=4)$', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Free_response_special', False)

    # forced response
    # under natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_special_under', False)
    # above natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(4*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(4t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_special_over', False)
    # at natural frequency
    y, t = smd.rk4(smd.dynamics, [0,0], 0, 20, 150, [m, c, k, lambda x,t: 10*math.sin(2*t)])
    smd.plot(t, [[k1[0] for k1 in y],[k1[1] for k1 in y]], r'State variables vs time ($m=1, c=2, k=4$; $f = sin(2t)$)', \
        'time (in secs)', ['Position', 'Velocity'], True, 'Forced_response_special_natural', False)            

################ Main ################

def main():
    plot_underdamped()
    plot_critically_damped()
    plot_overdamped()
    plot_special_case()

if __name__ == '__main__':
    main()    