from math import*
x=int(input("x ni kiriting:"))
y=int(input("y ni kiriting:"))
z=int(input("z ni kiriting:"))
a=abs(pow(x,y/x)-sqrt(y/x))+(y-x)*(cos(y)-z/(y-x))/(1+pow((y-x),2))
print(a)
