bool_to_int = lambda value : int(value)
print(bool_to_int(True))
print(bool_to_int(False))

get_smaller = lambda a,b : a if a < b else b
print(get_smaller(16,31))
print(get_smaller(253,223))

def cube(base):
 base = base**3
 return base
print(cube(2))
print(cube(5))

def absolute_difference(a,b):
  absolute_difference = b - a
  return abs(absolute_difference)
print(absolute_difference(14, 11))
print(absolute_difference(13, 40))

def squared_different(a,b):
  squared_different = abs(b-a) ** 2
  return squared_different
print(squared_different(14,11))
print(squared_different(13,40))

def hours_to_minutes(hours):
  hours = hours * 60
  return hours
print(hours_to_minutes(hours= 3.5))
print(hours_to_minutes(hours= 12))

def get_circumference(radius):
  circumference = 2 * 3.141592653589793 * radius
  return circumference
print(get_circumference(radius = 1))
print(get_circumference(radius= 9.2))

def linear_transform(x, slope, intercept):
  linear_transform = (x * slope) + intercept
  return linear_transform
print(linear_transform(slope= 5.0, x= 3.0, intercept= -8.5))
print(linear_transform(slope= -2.1, x= 2.5, intercept= 17.0))

def standardize(x, x_center, scale_size):
  standardize = (x-x_center) / scale_size
  return standardize
print(standardize(x= 8.2, x_center= 13.8, scale_size= 4.83))
print(standardize(x=2.89, x_center=-72.813, scale_size=24.63))
