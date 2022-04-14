import numpy as np

# Newton's method -- UNFINISHED

x0 = [1,1]

formula = lambda x: [x[0]-x[1]**3, x[1]**2+x[1]**2-1]
derivative = lambda x: [[1,-3*x[1]**2],[2*x[0],2*x[1]]]

def newtonsMethod(x0, f, d, n):
    for i in range(n+1):
        dn = np.dot(np.linalg.inv(d(x0)), f(x0))
        print(i)
        print("X0: ", x0)
        print("F: ",f(x0))
        print("J\'",d(x0))
        print("dn: ",dn)
        print()
        x0 = x0-dn

def main():
    newtonsMethod(x0, formula, derivative, 5)

if __name__ == "__main__":
    main()