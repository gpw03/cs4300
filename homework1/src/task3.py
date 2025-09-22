# Check if the given value is zero, greater than, or less than
def check_sign(a: int) -> str:
    if a > 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"

# Adding the first 10 prime numbers to a list then returning the list
def print_prime_nums() -> list[int]:
    primes = []
    count = 0
    num = 2

    # This checks count to make sure we have not already added 10 numbers
    while count < 10:
        # calling function to check if prime, if so append to list
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    return primes

# Checking if a given int if print for print prime function
def is_prime(N: int):
    # Checking each value to see if it goes into the given int
    for i in range(2, N):
        if N % i == 0:
            return False # Return if a number goes into N
    return True  # Return if no number goes into N

# Returning the value of the summation from 1 to 100
def one_to_hundred() -> int:
    # Count is added to sum and also used to make sure we are only going to 100
    count = 2 
    sum = 1 # Return value
    
    while count <= 100:
        sum += count
        count += 1
    return sum

if __name__ == "__main__":
    sign_1 = check_sign(-1)
    sign_2 = check_sign(0)
    sign_3 = check_sign(1)
    print(f"-1 sign: {sign_1}")
    print(f"0 sign: {sign_2}")
    print(f"1 sign: {sign_3}")
    primes = print_prime_nums()
    print(f"Primes: {primes}")
    is_5_prime = is_prime(5)
    is_20_prime = is_prime(20)
    print(f"5 is prime: {is_5_prime}")
    print(f"20 is prime: {is_20_prime}")
    full_count = one_to_hundred()
    print(f"Addition of every number from 1 to 100 = {full_count}")