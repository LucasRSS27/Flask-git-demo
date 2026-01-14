import numpy as np
import matplotlib.pyplot as plt
def shannon() :
    fig, axarr = plt.subplots(2, 2, figsize=(16,8))
    x=np.linspace(0,1,1000)
    def signal(x) :
        return np.sin(10*np.pi*x)
    f=5

    points=1/(10.5*f)*np.arange(10.5*f)
    plot1=axarr[0,0]
    plot1.set_title('Echantillonage à 10.5fM (très fin)')
    plot1.plot(x,signal(x))
    plot1.plot(points,signal(points),'o')

    points=1/(2.01*f)*np.arange(2.01*f)
    plot2=axarr[0,1]
    plot2.set_title('Echantillonage à 2.01fM (cas limite)')
    plot2.plot(x,signal(x))
    plot2.plot(points,signal(points),'o')

    points=1/(0.9*f)*np.arange(0.9*f)
    plot3=axarr[1,0]
    plot3.set_title('Echantillonage à 0.9fM (repliement de spectre)')
    plot3.plot(x,signal(x))
    plot3.plot(points,signal(points),'o')

    factor=11
    points=1/factor*np.arange(factor)
    def signal3(x) :
        return np.sin((1.3*np.pi +2*np.pi*factor)*x)
    def signal2(x) :
        return np.sin(1.3*np.pi*x)
    plot4=axarr[1,1]
    plot4.set_title('Autre exemple de repliement')

    plot4.plot(x,signal3(x),label='haute fréquence')
    plot4.plot(points,signal2(points),'o',label='échantillonnage')
    plot4.plot(x,signal2(x),label='basse fréquence')
    plot4.legend()

    plt.show()