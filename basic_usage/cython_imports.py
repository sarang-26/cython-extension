#import helloworld
import time
from fibonacci import fib

def fibonacci_python(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

start_time = time.time()
result_1 = fibonacci_python(10000000)
end_time = time.time()

print(f"Result: {result_1}")
print(f"Time taken in Python: {end_time - start_time} seconds")


# Now let's time this
start_time = time.time()
result_2 = fib(10000000)
end_time = time.time()

print(f"Result: {result_2}")
print(f"Time taken in Cython: {end_time - start_time} seconds")
