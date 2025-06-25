from linaris.geometry.vector import Vector2D
import math
import numpy as np

class InvalidLineError(Exception):
     pass
class InvalidPointsError(Exception):
     pass

class Line2D:
     def __init__(self,slope,y_intercept, name=""):
          """Initializes a line based on the equation y = mx + c"""
          
          self.slope = slope
          self.y_intercept = y_intercept
          self.name = name
     @classmethod
     def from_general_form(cls, a,b,c):
          """Initializes a line based on the equation ax + by + c = 0"""
          
          slope = -a/b
          y_intercept = -c/b
          return cls(slope=slope,y_intercept=y_intercept)
     
     @classmethod
     def from_points(cls, p1, p2):
          """Initializes a line based on the two points it passes. Accepts vector instances"""
          Line2D._validate_point(p1,p2)
          
          slope = (p2[1] - p1[1])/(p2[0] - p1[0])
          y_intercept = -slope*p1[0] + p1[1]
          return cls(slope=slope,y_intercept=y_intercept)

     def __repr__(self):
          return f"Line2D(slope={self.slope}, y_intercept={self.y_intercept})"
     
     def distance_from_point(self, point):
          """Calculates perpendicular distance from the point (a,b)"""
          Line2D._validate_point(point)
          
          return abs(point[1]-self.slope*point[0]-self.y_intercept)/math.sqrt(1+self.slope**2)
     
     def get_y(self, x):
          """Returns the ordinate for the subsequent abscissa"""
          
          return self.slope*x + self.y_intercept
     
     def get_x(self, y):
          """Returns the abscissa for the subsequent ordinate"""
          
          return (y-self.y_intercept)/self.slope
     
     def residual(self, point):
          """
          Returns the **residual** of the point from the line.

          The residual is the **vertical difference** between the point's y-value
          and the line's y-value at the same x-coordinate.

          **Formula:**
               residual = yₚ - (m * xₚ + c)
          """
          Line2D._validate_point(point)
          
          return point[1] - self.get_y(point[0])
     
     def is_parallel(self, line, tol=1e-7):
          """Returns True if the line is parallel"""
          if not isinstance(line, Line2D):
               raise InvalidLineError(f"Expected <class = 'Line2D'>. Received {type(line)}")
          
          if abs(line.slope - self.slope)<tol:
               return True
          return False
     
     def is_perpendicular(self, line):
          """Returns True if the line is perpendicular to this line, Flase otherwise"""
          if not isinstance(line, Line2D):
               raise InvalidLineError(f"Expected <class = 'Line2D'>, received {type(line)}")

          if line.slope*self.slope==-1:
               return True
          return False
     
     def contains_point(self, point):
          """Returns True if the point lies on the lines, False otherwise"""
          Line2D._validate_point(point)
          
          if point[1] == self.slope*point[0] + self.y_intercept:
               return True
          return False   
     
     def intersection_point(self, line):
          """If the line intersects this, returns the point else raises an exception"""
          if not isinstance(line, Line2D):
               raise InvalidLineError(f"Expected <class = 'Line2D'>, received {type(line)}")
          
          A = np.array([
               [1,-self.slope],
               [1, -line.slope]
          ])
          B = np.array([self.y_intercept, line.y_intercept])
          
          try:
               y,x = np.linalg.solve(A,B)
          except np.linalg.LinAlgError:
               raise InvalidLineError("Invalid Line since it either contains infinitely many number of solutions or no solutions at all")
          
          return Vector2D(x,y,name=f"I({self.name}-{line.name})")
          
     
     def as_feature_vector(self):
          "Returns the line in the form <slope,intercept> vector"
          
          return Vector2D(self.slope, self.y_intercept, name=f"Vector2D({self.name})")
     
     @staticmethod     
     def _validate_point(*points):
          """Checks wether the points are valid set of points."""
          
          for point in points:
               if not (isinstance(point, Vector2D) or isinstance(point, tuple)):
                    raise InvalidPointsError("The points passed are not valid points. Expected tuples or vectors.")
               elif isinstance(point, tuple) and len(point)!=2:
                    raise InvalidPointsError("Invalid points. Exptected a tuple with two flaoting numbers")
               
     @property
     def angle(self):
          """Returns the angle made by the line with the x - axis"""
          return math.atan(self.slope)
     
     @property
     def intercept(self):
          """Returns the y-intercept of the line"""
          return self.y_intercept
     
     @property
     def equation(self):
          return f"y = {self.slope}x + {self.y_intercept}"
               