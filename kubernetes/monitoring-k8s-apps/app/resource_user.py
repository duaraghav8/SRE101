# Time Complexity: O(2^n)
# Space Complexity: O(1)
def high_cpu_low_mem(n):
    for i in range(2**n):
        _ = i+1


# Time Complexity: O(2^n)
# Space Complexity: O(n^2)
def high_cpu_high_mem(n):
    long_str = " " * (n*n)
    for i in range(2**n):
        _ = i+1


# Time Complexity: O(1)
# Space Complexity: O(1)
def low_cpu_low_mem(n):
    x = n + 1


# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def med_cpu_high_mem(n):
    long_str = " " * (n*n)

