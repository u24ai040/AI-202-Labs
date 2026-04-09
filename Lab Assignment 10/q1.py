import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data=pd.read_csv("/content/cities.csv")
df=data.iloc[:,[0,1]].values

mx=df[:,0].min()
my=df[:,1].min()
Mx=df[:,0].max()
My=df[:,1].max()

points=set()

while len(points)<3:
    x=np.random.uniform(mx,Mx)
    y=np.random.uniform(my,My)
    points.add((x,y))

points=np.array(list(points))

def assign_cities(points,df):
    initial_nearest_airport=[]
    for i in range(len(df)):
        min_dist=float('inf')
        ans=0
        for j in range(len(points)):
            c=df[i][0]
            d=df[i][1]
            dist=((c-points[j][0])**2+(d-points[j][1])**2)
            if dist<min_dist:
                ans=j
                min_dist=dist
        initial_nearest_airport.append(ans)
    return initial_nearest_airport

def total_cost(points,df,initial_nearest_airport):
    cost=0
    for i in range(len(df)):
        ap=points[initial_nearest_airport[i]]
        c=df[i][0]
        d=df[i][1]
        dist=((c-ap[0])**2+(d-ap[1])**2)
        cost+=dist
    return cost

def compute_gradient(points,df,initial_nearest_airport):
    gradients=np.zeros_like(points)
    initial_nearest_airport=np.array(initial_nearest_airport)
    for i in range(len(points)):
        group=df[initial_nearest_airport==i]
        if len(group)==0:
            continue
        gradients[i,0]=2*np.sum(points[i,0]-group[:,0])
        gradients[i,1]=2*np.sum(points[i,1]-group[:,1])
    return gradients

def gradient_descent(df,points,alpha=0.01,max_iter=500):
    airports=points.copy()
    for iteration in range(max_iter):
        assignments=assign_cities(airports,df)
        grad=compute_gradient(airports,df,assignments)
        airports=airports-alpha*grad
        if np.max(np.abs(grad))<1e-6:
            print(f"Converged at iteration {iteration}")
            break
    return airports,assign_cities(airports,df)

def newton_raphson(df,points,max_iter=100):
    airports=np.array(points).copy()
    for iteration in range(max_iter):
        assignments=np.array(assign_cities(airports,df))
        old_airports=airports.copy()
        for i in range(len(airports)):
            Group=df[assignments==i]
            if len(Group)==0:
                continue
            n_i=len(Group)
            grad_x=2*np.sum(airports[i,0]-Group[:,0])
            grad_y=2*np.sum(airports[i,1]-Group[:,1])
            H_xx=2*n_i
            H_yy=2*n_i
            airports[i,0]=airports[i,0]-(1/H_xx)*grad_x
            airports[i,1]=airports[i,1]-(1/H_yy)*grad_y
        if np.max(np.abs(airports-old_airports))<1e-6:
            print(f"Converged at iteration {iteration}")
            break
    return airports,assign_cities(airports,df)

gd_airports,gd_assignments=gradient_descent(df,points)
nr_airports,nr_assignments=newton_raphson(df,points)

print("Gradient Descent Airports:")
print(gd_airports)

print("Newton Raphson Airports:")
print(nr_airports)

plt.scatter(df[:,0],df[:,1],c='blue',label='Cities')
plt.scatter(gd_airports[:,0],gd_airports[:,1],c='red',marker='x',s=200,label='GD Airports')
plt.scatter(nr_airports[:,0],nr_airports[:,1],c='green',marker='o',s=200,label='NR Airports')
plt.legend()
plt.show()