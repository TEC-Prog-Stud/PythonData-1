#!/usr/bin/env python3
__version__ = "1.0"
__author__ = "Pandadika"
import math

def hypothenuse(a ,b):
  """Calculate hypnothenuses

  Args:
      a (nubmer): lenght
      b (number): height

  Returns:
      number: hypothenuses
  """
  return math.sqrt(a**2+b**2)

def area(a, b):
  """Calcualte Area

  Args:
      a (number): height
      b (number): lenght

  Returns:
      number: area
  """
  return a*b/2