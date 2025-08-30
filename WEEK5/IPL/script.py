import numpy, random, math, os

def reorderQueue(length, offset, skip):
    l = length
    arr = [i for i in range(l)]
    current = offset - 1
    reordered = []
    if skip < 0:
        skip -= 1
        current = (current + 1) % l
    while l > 0:
        current = (current + skip) % l
        reordered.append(arr.pop(current))
        current = current % l
        l -= 1

    return reordered


os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def write(index, length, offset, skip):
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{length} {offset} {skip}\n")
        print(length, offset, skip)

    result = reorderQueue(length, offset, skip)
    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(" ".join(map(str, result)) + "\n")

for index in range(10):
    if index < 5:
        limit = 100
    else:
        limit = int(1e5)
    length = random.randint(1, limit)
    offset = random.randint(1, length)
    skip = random.randint(-length, length)
    write(index, length, offset, skip)

limit = int(1e5)

index = 10
length = 20
offset = 15
skip = -4
write(index, length, offset, skip)

index = 11
length = 20
offset = 15
skip = 4
write(index, length, offset, skip)

index = 12
length = limit
offset = limit
skip = -1
write(index, length, offset, skip)

index = 13
length = limit
offset = limit
skip = limit
write(index, length, offset, skip)

index = 14
length = limit
offset = 0
skip = -limit
write(index, length, offset, skip)

index = 15
length = limit
offset = random.randint(1, length)
skip = 1
write(index, length, offset, skip)