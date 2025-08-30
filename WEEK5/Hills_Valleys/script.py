import numpy, random, math, os

def countIt(nums,n):
        count = 0
        arr = []
        for i in range(len(nums)):
            if arr:
                if arr[-1]!=nums[i]:
                    arr.append(nums[i])
            else:
                arr.append(nums[i])
        #print(arr)
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
                #print(i)
                count += 1
        return count

limit = int(1e3)

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def write(index, length, arr):
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{length}\n")
        f.write(" ".join(map(str, arr)) + "\n")
        print(index, length)

    result = countIt(arr, length)
    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{result}\n")

for index in range(10):
    length = random.randint(3, limit)
    arr = numpy.random.randint(1, limit, size=length).tolist()
    write(index, length, arr)

index = 10
length = len([2,4,1,1,6,5])
arr = [2,4,1,1,6,5]
write(index, length, arr)

index = 11
length = len([6,6,5,5,4,1])
arr = [6,6,5,5,4,1]
write(index, length, arr)

index = 12
length = 1000
arr = numpy.random.randint(1, limit, size=length).tolist()
arr.sort()
write(index, length, arr)

index = 13
length = 1000
arr = [69]*1000
write(index, length, arr)

index = 14
length = 1000
arr = numpy.random.randint(1, limit, size=length).tolist()
arr.sort(reverse=True)
write(index, length, arr)

index = 15
length = 1000
arr = [random.randint(1, limit), random.randint(1, limit)] * 500
write(index, length, arr)