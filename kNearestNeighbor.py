from typing import List
import math
import numpy as np # learn more: https://python.org/pypi/numpy

def euclidean_distance(u: List[int], v: List[int]) -> float:
  # TODO: your euclidean function here
  sumeuclid = sum([(a - b) ** 2 for a, b in zip(u, v)])
  return math.sqrt(sumeuclid)

# Inputs
trains = []
labels = []
for i in range(1, 5):
  strings = input().split()
  ints = [int(x) for x in strings]
  trains.append(ints)
  labels.append(input())
test_strings = input().split()
test = [int(x) for x in test_strings]

# TODO: process the inputs
distances = []

label_index = 0
for i in range(len(trains)):
  distances.append(euclidean_distance(test,trains[i]))

top_distance = max(distances)
for i in range(len(distances)):
  if top_distance > distances[i] :
    top_distance = distances[i]
    label_index = i

# TODO: print outputs
for distance in distances:
  print("%.04f" % distance)



print(labels[label_index])