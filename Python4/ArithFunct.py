from math import *

def ADD(f, g):
  def h(x):
    if callable(f) and callable(g):
      return f(x) + g(x)
    elif callable(f):
      return f(x) + g
    elif callable(g):
      return f + g(x)
    else:
      return f + g
  return h

def SUB(f, g):
  def h(x):
    if callable(f) and callable(g):
      return f(x) - g(x)
    elif callable(f):
      return f(x) - g
    elif callable(g):
      return f - g(x)
    else:
      return f - g
  return h

def MUL(f, g):
  def h(x):
    if callable(f) and callable(g):
      return f(x) * g(x)
    elif callable(f):
      return f(x) * g
    elif callable(g):
      return f * g(x)
    else:
      return f * g
  return h

def DIV(f, g):
  def h(x):
    if callable(f) and callable(g):
      return f(x) / g(x)
    elif callable(f):
      return f(x) / g
    elif callable(g):
      return f / g(x)
    else:
      return f / g
  return h
