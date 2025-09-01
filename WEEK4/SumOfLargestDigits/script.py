def sumOfLargestDigits(nums, N):
    total = 0
    for num in nums:
        max_digit = 0
        if num == 0:
            max_digit = 0
        else:
            while num > 0:
                max_digit = max(max_digit, num % 10)
                if max_digit == 9:  # early stop
                    break
                num //= 10
        total += max_digit
    return total


limit_sets = [10, 100, 10000, 1000000]  # scale N
limit_val = (1 << 31) - 1               # max element
import os, numpy

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

for idx in range(10):
    lim = limit_sets[min(idx // 3, len(limit_sets) - 1)]
    N = numpy.random.beta(a=1, b=0.5)  # bias towards larger sizes
    N = int(1 + N * (lim - 1))
    arr = numpy.random.randint(0, limit_val + 1, size=N).tolist()

    with open(f"input/input{idx:02d}.txt", "w") as f:
        f.write(f"{N}\n")
        f.write(" ".join(map(str, arr)))

    ans = sumOfLargestDigits(arr, N)
    with open(f"output/output{idx:02d}.txt", "w") as f:
        f.write(f"{ans}\n")
    print(f"{idx} {N} {ans}")

idx = 10
N = 1000000
arr = numpy.random.randint(0, limit_val + 1, size=N).tolist()
with open(f"input/input{idx:02d}.txt", "w") as f:
    f.write(f"{N}\n")
    f.write(" ".join(map(str, arr)))
ans = sumOfLargestDigits(arr, N)
with open(f"output/output{idx:02d}.txt", "w") as f:
    f.write(f"{ans}\n")
print(f"{idx} {N} {ans}")

idx = 11
N = 100
arr = [0] * N
with open(f"input/input{idx:02d}.txt", "w") as f:
    f.write(f"{N}\n")
    f.write(" ".join(map(str, arr)))
ans = sumOfLargestDigits(arr, N)
with open(f"output/output{idx:02d}.txt", "w") as f:
    f.write(f"{ans}\n")
print(f"{idx} {N} {ans}")

idx = 12
N = 100
arr = [limit_val] * N
with open(f"input/input{idx:02d}.txt", "w") as f:
    f.write(f"{N}\n")
    f.write(" ".join(map(str, arr)))
ans = sumOfLargestDigits(arr, N)
with open(f"output/output{idx:02d}.txt", "w") as f:
    f.write(f"{ans}\n")
print(f"{idx} {N} {ans}")

idx = 13
N = 1
arr = [numpy.random.randint(0, limit_val + 1)]
with open(f"input/input{idx:02d}.txt", "w") as f:
    f.write(f"{N}\n")
    f.write(" ".join(map(str, arr)))
ans = sumOfLargestDigits(arr, N)
with open(f"output/output{idx:02d}.txt", "w") as f:
    f.write(f"{ans}\n")
print(f"{idx} {N} {ans}")

idx = 14
arr = [123, 45, 9]
N = len(arr)
with open(f"input/input{idx:02d}.txt", "w") as f:
    f.write(f"{N}\n")
    f.write(" ".join(map(str, arr)))
ans = sumOfLargestDigits(arr, N)
with open(f"output/output{idx:02d}.txt", "w") as f:
    f.write(f"{ans}\n")
print(f"Generated test {idx}: fixed sample, Ans={ans}")

idx = 15
arr = [0, 98, 1001, 56789]
N = len(arr)
with open(f"input/input{idx:02d}.txt", "w") as f:
    f.write(f"{N}\n")
    f.write(" ".join(map(str, arr)))
ans = sumOfLargestDigits(arr, N)
with open(f"output/output{idx:02d}.txt", "w") as f:
    f.write(f"{ans}\n")
print(f"Generated test {idx}: fixed sample, Ans={ans}")
