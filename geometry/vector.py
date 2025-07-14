import math
from sympy import Expr,sqrt

class Vec:
     def __init__(self, *components, name = "", check=True):
          if check:
               for component in components:
                    if not (isinstance(component, int) or isinstance(component, float)):
                         raise Exception("Invalid vector component")
               
          self.name = name
          
          self.components = list(components)
          
     def __getitem__(self, index):
          """
          Returns the component at the given index
          """
          return self.components[index]
          
     def __len__(self):
          """
          Returns the number of components in the vector
          """
          return len(self.components)
     
     def __iter__(self):
          return iter(self.components)
     
     def __add__(self, other):
          """
          Adds two vectors
          """
          if not(isinstance(other, Vec) and len(self) == len(other)):
               raise Exception("Invalid operands or invalid vector dimensions")
          
          zipped = zip(self.components, other.components)
          summed = [a+b for a,b in zipped]
          return Vec(*summed)
     
     def __sub__(self, other):
          """
          Subtracts two vectors
          """
          if not(isinstance(other, Vec) and len(self) == len(other)):
               raise Exception("Invalid operands or invalid vector dimensions")
          
          zipped = zip(self.components, other.components)
          sub = [a-b for a,b in zipped]
          return Vec(*sub)
     
     def __mul__(self, scalar):
          """
          Returns the product of scalar multiplication
          """
          multiplied = [a*scalar for a in self.components]
          return Vec(*multiplied)
     
     def __rmul__(self, scalar):
        return self.__mul__(scalar)
     
     def __truediv__(self, scalar):
          """
          Divides the vector by a scalar
          """
          
          if scalar == 0:
               raise ZeroDivisionError("Cannot divide by zero")
          
          return Vec(*[a/scalar for a in self.components])
     
     def __repr__(self):
          """
          String representation of the vector
          """
          string = ",".join([str(a) for a in self.components])
          return f"{self.name}<{string}>"
     
     def __eq__(self, other):
          """
          Comparison operation 
          """
          return isinstance(other, Vec) and self.components == other.components
     
     @property
     def magnitude(self):
          """Returns the magnitude of the vector"""
          
          squared = [a**2 for a in self.components]
          summed = sum(squared)
          
          if all([isinstance(a,(int, float)) for a in self.components]):
               return math.sqrt(summed)
          return sqrt(summed)
               
          
     
     def dot(self, vector):
          """
          Returns the dot product of the currect vector with the passed vector
          """
          if not isinstance(vector, Vec):
               raise Exception("Parameter is not a vector")
          
          assert len(vector)==len(self)      # checks for correct dimensions
          
          zipped = zip(vector.components, self.components)
          product = [a*b for a,b in zipped]
          return sum(product)
     
     def normalize(self):
          """
          Returns the unit vector in the direction of the vector
          """
          magnitude = self.magnitude()
          if magnitude==0:
               raise ValueError("Cannot nomalize a null vector")
          
          return Vec(*[a/magnitude for a in self.components])
     
     def set_val(self, index, value):
          """
          Sets the value at the index
          """
          self.components[index] = value
     
     
class Vector2D(Vec):
     def __init__(self, i,j, name="", check:bool=True):
          super().__init__(i,j, name=name, check=check)
          
     @property
     def x(self):
          """
          Returns the horizontal component of the vector
          """
          
          return self.components[0]
     @property
     def y(self):
          """Returns the vertical component of the vector"""
          
          return self.components[1]
     
     @property
     def i(self):
          """
          Returns the horizontal component of the vector
          """
          
          return self.x
     
     @property
     def j(self):
          """
          Returns the vertical component of the vector
          """
          
          return self.y
     
     def set_x(self,x):
          """
          Setter function for the horizontal component
          """
          if not (isinstance(x, int) or isinstance(x, float)):
                    raise Exception("Invalid vector component")
          
          self.components[0] = x
          
     def set_y(self,y):
          """
          Setter function for the vertical component
          """
          if not (isinstance(y, int) or isinstance(y, float)):
                    raise Exception("Invalid vector component")
          
          self.components[1] = y
          
     
class Vector3D(Vec):
     def __init__(self, i,j,k, name = "", check:bool = True):
          super().__init__(i,j,k, name=name, check=check)
          
     @property
     def x(self):
          """
          Returns the horizontal component of the vector
          """
          
          return self.components[0]
     @property
     def y(self):
          """Returns the vertical component of the vector"""
          
          return self.components[1]
     
     @property
     def z(self):
          """Retuns the component that is perpendicular to the plane"""
          
          return self.components[2]
     
     @property
     def i(self):
          """
          Returns the horizontal component of the vector
          """
          
          return self.x
     
     @property
     def j(self):
          """
          Returns the vertical component of the vector
          """
          
          return self.y
     
     @property
     def k(self):
          """Retuns the component that is perpendicular to the plane"""
          
          return self.z
     
     def set_x(self,x):
          """
          Setter function for the horizontal component
          """
          if not (isinstance(x, int) or isinstance(x, float)):
                    raise Exception("Invalid vector component")
          
          self.components[0] = x
          
     def set_y(self,y):
          """
          Setter function for the vertical component
          """
          if not (isinstance(y, int) or isinstance(y, float)):
                    raise Exception("Invalid vector component")
          
          self.components[1] = y
          
     def set_z(self,z):
          """
          Setter function for the vertical component
          """
          if not (isinstance(z, int) or isinstance(z, float)):
                    raise Exception("Invalid vector component")
          
          self.components[2] = z