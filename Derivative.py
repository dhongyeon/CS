import numpy as np
import pylab as plt
import seaborn as sns
import pandas as pd

class Derivative:
  def __init__(self, f, h=10**(-5)):
      self.f = f
      self.h = float(h)

  def __call__(self, x):
      return (self.f(x+self.h) - self.f(x))/self.h



