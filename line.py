from vector import Vector2D
import math

class Line2D:
     def __init__(self,slope,y_intercept):
          """Initializes a line based on the equation y = mx + c"""
          
          self.slope = slope
          self.y_intercept = y_intercept
     @classmethod
     def from_general_form(cls, a,b,c):
          """Initializes a line based on the equation ax + by + c = 0"""
          
          slope = -a/b
          y_intercept = -c/a
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
     
     @staticmethod     
     def _validate_point(*points):
          """Checks wether the points are valid set of points."""
          
          for point in points:
               if not (isinstance(point, Vector2D) or isinstance(point, tuple)):
                    raise Exception("The points passed are not valid points. Expected tuples or vectors.")
               elif isinstance(point, tuple) and len(point)!=2:
                    raise Exception("Invalid points. Exptected a tuple with two flaoting numbers")
               
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
               