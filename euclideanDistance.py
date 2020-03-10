from typing import List 
import math

def euclidean(u: List[float], v: List[float]) -> float:
  # TODO: Fix this with Euclidean distance formula
  # Both has 5 floating point numbers
  sumeuclid = sum([(a - b) ** 2 for a, b in zip(u, v)])
  return math.sqrt(sumeuclid)

a = [float(input()), float(input()), float(input()), float(input()), float(input())]
b = [float(input()), float(input()), float(input()), float(input()), float(input())]
result = euclidean(a, b)
print("%.4f" % result)
