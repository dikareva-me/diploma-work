import numpy as np
from matplotlib import pyplot as plt
from main import y_calc




def get_a_b(a, n, E, I, k, h):
    A = np.zeros((sum(n)+1, sum(n)+1))
    b = np.zeros(sum(n)+1)

    A[0, 0] = 2+k*h**4/(E*I)
    A[0, 1] = -4
    A[0, 2] = 2
    b[0] = 0
    print(*A[0])

    A[1, 0] = -2
    A[1, 1] = 5 + k*h**4/(E*I)
    A[1, 2] = -4
    A[1, 3] = 1
    b[1] = 0
    print(*A[1])

    #1 отрезок = 0
    for i in range(2, n[0]+n[1]+n[2]+n[3]-1):
        A[i, i-2] = 1
        A[i, i-1] = -4
        A[i, i] =  6 + k*h**4/(E*I)
        A[i, i+1] = -4
        A[i, i+2] = 1
        b[i] = 0
        print(*A[i])
    
    b[n[0]] = k*a*h**4/(2*E*I)


    # #2 отрезок = kah/ei
    for i in range(n[0]+1, n[0]+n[1]+1):
    #     A[i, i-2] = 1
    #     A[i, i-1] = -4
    #     A[i, i] =  6 + k*h**4/(E*I)
    #     A[i, i+1] = -4
    #     A[i, i+2] = 1
        b[i] = k*a*h**4/(E*I)
    #     print(*A[i])

    b[n[0]+n[1]] = k*a*h**4/(2*E*I)
    
    # #3 отрезок = 0
    for i in range(n[0]+n[1]+1, n[0]+n[1]+n[2]+1):
    #     A[i, i-2] = 1
    #     A[i, i-1] = -4
    #     A[i, i] =  6 + k*h**4/(E*I)
    #     A[i, i+1] = -4
    #     A[i, i+2] = 1
        b[i] = 0
    #     print(*A[i])

    b[n[0]+n[1]+n[2]] = k*a*h**4/(2*E*I)

    # #4 отрезок
    for i in range(n[0]+n[1]+n[2]+1, n[0]+n[1]+n[2]+n[3]-1):
    #     A[i, i-2] = 1
    #     A[i, i-1] = -4
    #     A[i, i] =  6 + k*h**4/(E*I)
    #     A[i, i+1] = -4
    #     A[i, i+2] = 1
        b[i] = k*a*h**4/(E*I)
    #     print(*A[i])

    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]-3] = 1
    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]-2] = -4
    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]-1] = 7 + k*h**4/(E*I)
    A[n[0]+n[1]+n[2]+n[3]-1, n[0]+n[1]+n[2]+n[3]] = -4
    b[n[0]+n[1]+n[2]+n[3]-1] = k*a*h**4/(E*I)
    print(*A[n[0]+n[1]+n[2]+n[3]-1])

    A[n[0]+n[1]+n[2]+n[3], n[0]+n[1]+n[2]+n[3]-2] = 2
    A[n[0]+n[1]+n[2]+n[3], n[0]+n[1]+n[2]+n[3]-1] = -8
    A[n[0]+n[1]+n[2]+n[3], n[0]+n[1]+n[2]+n[3]] = 6 + k*h**4/(E*I)
    b[n[0]+n[1]+n[2]+n[3]] = k*a*h**4/(E*I)
    
    print(*A[n[0]+n[1]+n[2]+n[3]])

    # #print(A)
    # for lst in A:
    #     for el in lst:
    #         print(f'{el:.{1}f}', end=' ')
    #     print()
    # Get b
   
    return A, b




if __name__ == "__main__":
    
    length = [0, 6.7, 15.6, 23.5, 27.45]

    a = 1.04833163e-05
    k= 80000
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
    for i in range(len(n)):
        for j in range(n[i]):
            x.append(l_round[i]+h*j)
    x.append(3.4)

    x_list = [i/m for i in x]
    A, b = get_a_b(a, n, 1, 1, 4,h)
    print(x)
    print(b)

    y = np.linalg.solve(A, b)
    print(y)


    plt.plot(x, y )     
    plt.xlabel("x")
    plt.ylabel("y, см")
    plt.grid()
    plt.show()



