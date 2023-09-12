# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:23:01 2022

@author: Alvaro Ascanio Sanchez
"""
#librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pnd
import math as mt

#cargue de datos
datos= pnd.read_csv('datos en planta.txt')
datosr= np.array(datos)

#Definiciones
def sen(grados):
    return np.sin(np.radians(grados))
def cos(grados):
    return np.cos(np.radians(grados))

#Variables 
A= datosr[:,0]
B= datosr[:,1]
H= datosr[:,2]
pi=mt.pi
#Variable para distancia horizontal
Dh=H*cos(B)
#
Dy=((cos(A))*Dh)
Dx=((sen(A))*Dh)
Dy1= Dy.tolist()
Dx1= Dx.tolist()
Nx=len(Dx)
Ny=len(Dy)


#Definiendo origenes de x    
listax=[]
listax.insert(0,0)
Nl=len(listax)

def automatico(x):
    return ((sum(Dx[0:x]))+Dx[x])

for i in range(Nx):      
    if(Nl<=Nx):      
        listax.append(automatico(i))
        Nl=len(listax)

        
        
Dezplazamiento_x= listax
origen= 0
#Definiendo origenes de y   

listay=[]
listay.insert(0,0)

Nl2=len(listay)

def automatico(y):
    return ((sum(Dy[0:y]))+Dy[y])

for p in range(Ny):      
    if(Nl2<=Ny): 
        
        listay.append(automatico(p))
        
        Nl2=len(listay)
        

#Interfaz

if all(A<=360) and all(B<=90):
    print('Direcciones de Azimut y Angulos cargados')
else:
    print('Asegurese que los datos esten correctos')

#definiendo dimensiones iguales para el gráfico.

Minimo=min(min(listay),min(listax))
Maximo=max(max(listay),max(listax))
x=np.linspace(Minimo-4,Maximo+4)
y=np.linspace(Minimo-4,Maximo+4)

#val deltas
def Consecutivos(n):
    return n+1
Delta=[]
Delta.insert(0,0)
lDelta=len(Delta)
for l in range(Nl2-1):
    if(lDelta<Nl2):
        Delta.append(Consecutivos(l))
Deltai=np.array(Delta)
        
#ploteando figura.
Ancho=abs((min(listax)+Minimo*0.10)-(max(listax)+Maximo*0.10))
Largo=abs((min(listay)+Minimo*0.10)-(max(listay)+Maximo*0.10))
RR=max(Ancho,Largo)
rr=min(Ancho,Largo)
Relacion1=RR/rr
Relacion2=rr/RR
Comp1= max(Relacion1,Relacion2)
Comp2= min(Relacion1,Relacion2)
if(Ancho>Largo):
    X1=20
    Y1=20*Relacion2
if(Ancho<Largo):
    Y1= 20
    X1=20* Relacion2
    
if (Ancho==Largo):
    X1=20
    Y1=20
        
fig= plt.figure()
fig.set_figheight(Y1)
fig.set_figwidth(X1)
plt.xlabel('Desplazamiento E-W [m]')
plt.ylabel('Desplazamiento N-S [m]')
plt.title('POLIGONAL VISTA EN PLANTA',fontsize= 15)
plt.xlim(min(listax)+Minimo*0.10,max(listax)+Maximo*0.10)
plt.ylim(min(listay)+Minimo*0.10,max(listay)+Maximo*0.10)


for i, label in enumerate(Delta):
    plt.text(listax[i], listay[i], label)

Xx=input("Nombre de Archivo: ")
plt.plot(listax,listay,'c', linewidth=1 ) 
plt.savefig(Xx+'.png')
print('Su imagen1 ha sido guardada como '+Xx+'.png')

###################################################################

#Creando perfil topográfico.

#Variables 
R=float(input('Ingrese la dirección de la vista auxiliar(rumbo promedio)'))
A= datosr[:,0]
B= datosr[:,1]
H= datosr[:,2]


Difx=((Dh*sen(R))-(Dh*sen(A)))
Dify=((Dh*cos(R))-(Dh*cos(A)))



Difx1=pow(Difx.T,2)
Dify1=pow(Dify.T,2)


Dift=np.sqrt(Difx1+Dify1)

Distancias=[]
Distancias.insert(0,0)

Num1=len(Dift)
Num=len(Distancias)

def Fundist(i):
    return ((sum(Dift[0:i]))+Dift[i])

for p in range(Num1):
    if(Num<=Num1):
        
        Distancias.append(Fundist(p))
        Num=len(Distancias)






    


