import numpy as np
import matplotlib.pyplot as plt

num1 = int(input("Enter the 1st number = "))
num2 = int(input("Enter the 2nd number = "))

x = num1
y = num2

def topla(num1, num2):
    return num1+num2

sonuc = topla(num1,num2)
print (num1, "+", num2, " = ", sonuc)

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()