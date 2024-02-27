from math import sinh, cosh, sin, cos, sqrt
from matplotlib import pyplot as plt
import numpy as np

def v1(x):
    return cosh(x)*cos(x)

def v2(x):
    return 1/2*(cosh(x)*sin(x)+sinh(x)*cos(x))

def v3(x):
    return 1/2*sinh(x)*sin(x)

def v4(x):
    return 1/4*(cosh(x)*sin(x)-sinh(x)*cos(x))

def coef_init(l = []):
    coef = np.zeros((3, 3))

    coef[0][0] = v4(l[-1])
    coef[0][1] = -1/4*v1(l[-1])
    for i in range(2, len(l)+1):
        coef[0][2] += (-1)**(i) * v4(l[-1] - l[i-2])
        print(l[-1] - l[i-2])
    coef[0][2] *= -1
#    print()


    coef[1][0] = v2(l[-1])
    coef[1][1] = v3(l[-1])
    for i in range(2, len(l)+1):
        coef[1][2] += (-1)**(i) * v2(l[-1] - l[i-2])
        print(l[-1] - l[i-2])
    coef[1][2] *= -1
#    print()



    for i in range(1, len(l)):
  #      print(l[i-1])
       # coef[2][0] += (-1)**i*v2(l[i-1])
        coef[2][0] += (-1)**(i+1)*v2(l[i-1])
  #  print()
    for i in range(1, len(l)):
  #      print(l[i-1])
        #coef[2][1] += (-1)**i*v3(l[i-1])
        coef[2][1] += (-1)**(i+1)*v3(l[i-1])
  #  print()
    for i in range(2, len(l)):
        for j in range(1, i):
   #         print(l[i-1]-l[j-1])
          #  coef[2][2] += (-1)**(i+j)*v2(l[i-1]-l[j-1])
            coef[2][2] += (-1)**(i+j+1)*v2(l[i-1]-l[j-1])
            print(l[i-1]-l[j-1])
   # coef[2][2] *= -1

    return coef


def y_calc(m, c1, c2, a, l):
    y_vec = []
    start = m
    stop = 30*m
    step = m
    iter = 0
    for x in np.arange(start, stop, step):
        iter += 1
        if x >= 0:
            y = v1(x)*c1+v2(x)*c2
        for i in range (2, len(l)+1):
            if x >= l[i - 2]:
                y += a * (-1)**(i) * (1 - v1(x - l[i-2]))
        y_vec.append(y )

    x = np.arange(start, stop, step)
    return x, y_vec



if __name__ == "__main__":
    # length = [6.7, 15.6, 23.5, 27.45]
    # T = 10.0
    # k= 80000
    # I= 3.97
    # E = 2.1 * (10**7)
    length = [6.7, 15.6, 23.5, 27.45]
    T = 10.0
    k= 80000
    I= 3.97
    E = 2.1 * (10**7)


    m = ( k/(4*E*I) )**0.25
    EIm3 = E * I * m ** 3
    EIm2 = E * I * m ** 2
    print(m, EIm2, EIm3)
    



    l = [i * m for i in length]
    print("lambda = ", l)

    b=[0, 0, T/(8*E * I * m ** 3)]
    coef = coef_init(l)
    print(coef)
    print(b)
    c = np.linalg.solve(coef, b)
    print(c)
    new_c = coef[:2,:2]
    # new_c = []
    # for i in range(2):
    #     for j in range(3):
    #         new_c[i][j] = coef[i][j]

    a = coef[:2, 2]
    x = np.linalg.solve(new_c, a)
    print(x)
    # for i in range(0,2):
    #     print(coef[i][0], coef[i][1], coef[i][2])
    x, y = y_calc(m, c[0], c[1], c[2], l)
  #  plt.semilogy(x, y)
    plt.plot(x, y, )
        
    plt.xlabel("x")
    plt.ylabel("y, см")
    plt.grid()
    plt.show()

