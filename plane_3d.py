# -*- coding: utf-8 -*-
"""Plane_3D.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKK2didw-1VwP6AeluCdbKEg7fn1l3sT
"""

#Q1-Plane representation with normal n and Point P0,P is the dot product of n and (P0,P),where P0 is point on P.
import numpy as np
class Plane:
  def __init__(self, normal, point):
    self.normal = normal
    self.point = point
    
  def calPlane(self):
    print("hi")
    #n = np.transpose(self.normal)
    a = self.normal.item(0)
    b = self.normal.item(1)
    c = self.normal.item(2)
    d1 = -(np.matmul(self.normal,np.transpose(self.point)))
    d1 = np.asscalar(d1)
    
    
    print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d1))
    #Assigning the d1 value as Point in class Plane.
    self.point = d1
    # Method to return values a , b , c , d
  # Q2-Method for displaying Plane parameters
  def Plane_param(self):
    print(" a = {0} , b = {1} , c = {2}, d = {3} ".format(self.normal.item(0),self.normal.item(1),self.normal.item(2),self.point))
  # Q3-Method for calculating distance of a point to a plane.
  def distance(self, Destination_point):
    a = self.normal.item(0)
    b = self.normal.item(1)
    c = self.normal.item(2)
    d = self.point
    Destination_point = np.asmatrix(Destination_point)
    
    point1 = np.matrix((a,b,c))
    numr = np.multiply(a,Destination_point.item(0)) + np.multiply(b,Destination_point.item(1)) + np.multiply(c,Destination_point.item(2)) + d
    deno = np.linalg.norm(point1-[0,0,0])
    if deno == 0:
      print("Distance from plane is infinity")
    else:
      dist = np.divide(numr,deno)
      print("distance = ",dist)

  
#parameters for a normal a,b,c
#parameters for a point x,y,z
nor = np.asmatrix([1,1,2])
p = np.asmatrix([1,2,3])
p1 = Plane(nor,p)
p1.calPlane()
p1.Plane_param()
p1.distance((1,2,3))

