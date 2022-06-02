import numpy as np

array = np.array([1, 2, 3])
print(array)
print(type(array))

print(50*'-')

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(type(array))
print(array.shape)

print(50*'-')

array = np.zeros((3, 4))
print(array)

print(50*'-')

array = np.zeros((3, 4), dtype=int)
print(array)

print(50*'-')

array = np.ones((3, 4))
print(array)

print(50*'-')

array = np.full((3, 4), 5, dtype=int)
print(array)

print(50*'-')

array = np.random.random((3, 4))
print(array)

print(array[0, 0])
print(50*'-')
print(array > 0.2)

print(50*'-')
filtered_array = array[array > 0.2]
print(filtered_array)
print(filtered_array.shape)

print(50*'-')

sum = np.sum(array)
print("Sum:", sum)

print("Ceiling:", np.ceil(array))

print("Floor:", np.floor(array))

print("Round:", np.round(array))

print(50*'-')

first = np.array([1, 2, 3, 4, 5])
second = np.array([6, 7, 8, 9, 10])

combined = first+second
print(combined)

print(50*'-')

nums = np.arange(2, 8)
print(type(nums))
print(nums)

nums = np.arange(2, 8, 2)
print(type(nums))
print(nums)

print(50*'-')

numbers = [1, 2, 3, 4, 5, 6, 7]
print(type(numbers))
doubled_numbers = [number*2 for number in numbers]
print(doubled_numbers)

numbers = np.array([1, 2, 3, 4, 5, 6, 7])
print(numbers)
doubled_numbers = numbers*2
print(doubled_numbers)
print(50*'-')
# Dimesions in inches -- > 3.4,5.6,7.8
# Dimensions into cms

dimensions_inch = np.array([3.4, 5.6, 6.7, 7.8])
print("Inches:", dimensions_inch)
dimensions_cm = dimensions_inch*2.54
print("CM:", dimensions_cm)

print(50*'-')

lin = np.linspace(1, 10, 10)
print(lin)

lin = np.linspace(1, 10, 30)
print(lin)

print(50*'-')

eye_matrix = np.eye(4)

print(eye_matrix)


print(50*'-')

numbers = np.arange(1, 17)
print(numbers)

reshaped_numbers = numbers.reshape(4, 4)
print(reshaped_numbers)

reshaped_numbers = numbers.reshape(8, 2)
print(reshaped_numbers)

reshaped_numbers = numbers.reshape(2, 8)
print(reshaped_numbers)

# reshaped_numbers = numbers.reshape(9, 4)
# print(reshaped_numbers)
# ValueError: cannot reshape array of size 16 into shape(9, 4)

print(50*'-')

random_values = np.random.randint(1, 100, 5)
print(random_values)

minimum = random_values.min()
print("Min:", minimum)

maximum = random_values.max()
print("Max:", maximum)

mean_value = random_values.mean()
print("Mean:", mean_value)

print(50*'-')

numbers = np.arange(1, 16)
print(numbers)
print(numbers[2])
print(numbers[1:8])
print(numbers[0:8])
print(50*'-')
numbers2D = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(numbers2D)
print(numbers2D[0, 0])
print(numbers2D[2, 2])
print(numbers2D[0])

print(50*'-')

# clip(a,a_min,a_max)

# Given an interval, values outside the interval are clipped to the interval
#  edges.
# For example, if an interval of[0, 1] is specified,
#  values smaller than 0 become 0, and values larger than 1 become 1.

numbers = [10, 20, 80, 98, 78, 65]

min = 30
max = 50

clipped = np.clip(numbers, min, max)
print("O:", numbers)
print("C:", clipped)
