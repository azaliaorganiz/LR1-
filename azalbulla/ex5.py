import copy
import math


values = [3,1,3,2,1,5,2]
unique_values = set(values)

other = set([2,4,5])

print(f"unique_set : {unique_values}")
print(f"кол-во уникальных элементов: {len(unique_values)}")

print(F"A & B : {unique_values & other}")
print(F"A | B : {unique_values | other}")

print(F"A - B : {unique_values - other}")
print(f"B - A : {other - unique_values}")