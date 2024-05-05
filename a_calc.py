import numpy as np
from matplotlib import pyplot as plt
from main import y_calc




def get_a_b(n, E, I, h, T, m):
    A = np.zeros((sum(n)+2, sum(n)+2))
    print(sum(n)+1)
    b = np.zeros(sum(n)+2)

    A[0, 0] = 2+4*h**4
    A[0, 1] = -4
    A[0, 2] = 2
    A[0, -1] = 0
    print(*A[0])

    A[1, 0] = -2
    A[1, 1] = 5 + 4*h**4
    A[1, 2] = -4
    A[1, 3] = 1
    print(*A[1])

    #1 отрезок = 0
    for i in range(2, n[0]+n[1]+n[2]+n[3]-1):
        A[i, i-2] = 1
        A[i, i-1] = -4
        A[i, i] =  6 + 4*h**4
        A[i, i+1] = -4
        A[i, i+2] = 1
        print(*A[i])
    
    A[n[0], -1] =2*h**4
    


    # #2 отрезок = kah/ei
    for i in range(n[0]+1, n[0]+n[1]+1):
        A[i, -1] = 4*h**4

    A[n[0]+n[1], -1] = 2*h**4

    for i in range(n[0]+n[1]+1, n[0]+n[1]+n[2]+1):
        A[i, -1] = 0

    A[n[0]+n[1]+n[2], -1] = 2*h**4

    for i in range(n[0]+n[1]+n[2]+1, n[0]+n[1]+n[2]+n[3]-1):
        A[i, -1] = 4*h**4
    

    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]-3] = 1
    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]-2] = -4
    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]-1] = 7 + 4*h**4
    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]] = -4
    A[n[0]+n[1]+n[2]+n[3]-1, -1] = 4*h**4
    print(*A[n[0]+n[1]+n[2]+n[3]-1])

    A[n[0]+n[1]+n[2]+n[3], n[0]+n[1]+n[2]+n[3]-2] = 2
    A[n[0]+n[1]+n[2]+n[3], n[0]+n[1]+n[2]+n[3]-1] = -8
    A[n[0]+n[1]+n[2]+n[3], n[0]+n[1]+n[2]+n[3]] = 6 + 4*h**4
    A[n[0]+n[1]+n[2]+n[3], -1] = 4*h**4

    A[-1, n[0]-2]=-1
    A[-1, n[0]-1]=2
    A[-1, n[0]+1]=-2
    A[-1, n[0]+2]=1

    A[-1, n[0]+n[1]-2]=1
    A[-1, n[0]+n[1]-1]= -2
    A[-1, n[0]+n[1]+1]= 2
    A[-1, n[0]+n[1]+2]=-1

    A[-1, n[0]+n[1]+n[2]-2]=-1
    A[-1, n[0]+n[1]+n[2]-1]=2
    A[-1, n[0]+n[1]+n[2]+1]=-2
    A[-1, n[0]+n[1]+n[2]+2]=1
    A[-1, -1] = -6*h**4

    b[-1] = -T*h**3/(E*I*m**3)

    
    print(*A[n[0]+n[1]+n[2]+n[3]])
    print(*A[-1])
    print([row[-1] for row in A])
    print(*b)

    return A, b




if __name__ == "__main__":
    
    length = [0, 6.7, 15.6, 23.5, 27.45]

    a = 1.04833163e-05
    k= 80000
    T = 10.0
    I= 3.97
    E = 2.1 * (10**7)
    m = ( k/(4*E*I) )**0.25
    l = [i * m for i in length]


    y_list = []
    x = []
    l_round = []

    h = 0.1
    l_round = [round(i, 1) for i in l]
    n = [int((l_round[i] - l_round[i-1])/h) for i in range(1, len(l))]
    print(l_round, n)
    # for i in range(len(n)):
    #     for j in range(n[i]):
    #         x.append(l_round[i]+h*j)
    # x.append(3.4)
    x = [i * 0.1 for i in range(34)]
    print(x)

    x_list = [i/m for i in x]
    A, b = get_a_b(n, E, I, h, T, m)
    print(b)
    # b=A[:,-1]
    # b=b[:-1]
    # A = A[:-1, :-1]
    

    y = np.linalg.solve(A, b)
    print(y)
    a = y[-1]
    print(a)

    y = y[:-1]
    plt.plot(x, y )     
    plt.xlabel("x")
    plt.ylabel("y, см")
    plt.grid()
    plt.show()



