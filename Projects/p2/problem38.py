import math
import matplotlib.pyplot as plt
import numpy as np

def bitreverse(n,s):
    a = 0
    for i in range(s):
        a = a*2+n%2
        n = math.floor(n/2)
    return a

def CooleyTukey(f):
    n = len(f)
    stages = int(math.log2(n))
    F = [f[bitreverse(i,stages)] for i in range(n)]
    W = math.e ** (-2*math.pi*complex(0,1)/n)
    stagenumber = 1
    for i in range(stages):
        stagenumber = stagenumber*2
        w = W ** (n/(2**(i+1)))
        b = [F[j]+(w**j)*F[j+int(stagenumber/2)] if (j%stagenumber)<stagenumber/2 else F[j-int(stagenumber/2)]+(w**j)*F[j] for j in range(n)]
        F = [b[i] for i in range(n)]
    return F

def main():
    param = 32
    f = [math.sin(0.2*math.pi*i) for i in range(param)]
    F = CooleyTukey(f)
    mode = [abs(F[i]) for i in range(param)]
    deg = [math.atan(F[i].imag/F[i].real)/math.pi*180 for i in range(param)]
    tf = np.fft.fft(f)
    tmode = [abs(tf[i]) for i in range(param)]
    tdeg = [math.atan(tf[i].imag/tf[i].real)/math.pi*180 for i in range(param)]
    plt.figure()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=None, hspace=0.4)
    plt.subplot(311)
    plt.stem(np.linspace(0,param-1,param),f)
    plt.title('Original')
    plt.subplot(312)
    plt.plot(np.linspace(0,param-1,param),tmode,color='coral')
    plt.stem(np.linspace(0,param-1,param),mode)
    plt.title('Magnitude of FFT')
    plt.subplot(313)
    plt.plot(np.linspace(0,param-1,param),tdeg,color='coral')
    plt.stem(np.linspace(0,param-1,param),deg)
    plt.title('Angle of FFT')
    plt.show()
    

if __name__ == '__main__':
    main()