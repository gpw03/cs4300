import numpy as np

# Input is a list of numbers, use numpy to calculate mean
def calculate_mean(nums: list):
    return np.mean(nums)

# Input is a list of numbers, use numpy to calculate median
def calculate_median(nums: list):
    return np.median(nums)    

# Input is 2 poijnts, use numpy to calculate dot product
def calculate_dot_product(a: list, b: list):
    return np.dot(a, b)

if __name__ == "__main__":
    mean_1 = calculate_mean([1, 2, 3, 4, 5])
    print(f"Mean of [1, 2, 3, 4, 5] is {mean_1}")
    median_1 = calculate_median([1, 2, 3, 4, 5])
    print(f"Mean of [1, 2, 3, 4, 5] is {median_1}")
    dot_prod = calculate_dot_product([1, 2], [3, 4])
    print(f"Dot Product of [1,2] and [3,4] is {dot_prod}")
