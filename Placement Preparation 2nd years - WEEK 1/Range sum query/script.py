import numpy as np
import random
import os

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

# 🔴 YOU MUST IMPLEMENT CORRECT SOLUTION HERE
def solve(nums, left, right):
    prefix = [0]*(len(nums)+1)
    pre = 0
    for idx,num in enumerate(nums):
        pre+=num
        prefix[idx+1] = pre 
    return prefix[right+1]-prefix[left]

def write(index, nums, left, right):
    n = len(nums)

    # Write input
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, nums)) + "\n")
        f.write(f"{left} {right}\n")

    # Generate correct output
    result = solve(nums, left, right)

    print(index, n, result)

    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(str(result) + "\n")

for index in range(25):
    if index < 5:
        # Small random
        n = random.randint(3, 10)
        nums = np.random.randint(-10, 10, size=n).tolist()
        left = random.randint(0, n-1)
        right = random.randint(left, n-1)
    elif index < 10:
        # Small random
        n = random.randint(3, 100)
        nums = np.random.randint(-10, 10, size=n).tolist()
        left = random.randint(0, n-1)
        right = random.randint(left, n-1)

    elif index < 14:
        # Small cases with left == right
        n = random.randint(3, 100)
        nums = np.random.randint(-10, 10, size=n).tolist()
        left = random.randint(0, n-1)
        right = left
    elif index < 20:
        # Large cases
        n = random.randint(100, 1000)
        nums = np.random.randint(-1000, 1000, size=n).tolist()
        left = random.randint(0, n-1)
        right = random.randint(left, n-1)
    else:
        # Large cases with left == right
        n = random.randint(1000, 10000)
        nums = np.random.randint(-1000, 1000, size=n).tolist()
        left = random.randint(0, n-1)
        right = left
    write(index, nums, left, right)

index = 25
n = 1000
nums = np.random.randint(-1000, 1000, size=n).tolist()
write(index, nums, 0, n-1)

index = 26
n = 1000
nums = [0]*n
write(index, nums, 100, 900)

index = 27
n = 100000
nums = np.random.randint(-1000, 1001, size=n).tolist()
write(index, nums, 0, n-1)