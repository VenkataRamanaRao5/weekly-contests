import numpy, random, math, os

def hotelReservations(reservation):
    p1 = reservation.split('|')
    q = [list(map(int,num.split(','))) for num in p1]
    
    maxi = 0
    for a,b in q:
        maxi = max(maxi,a,b)
    
    pre = [0]*(maxi+2)
    for start,end in q:
        pre[start]+=1
        pre[end+1]-=1
    
    curr = 0
    for i in range(len(pre)):
        curr += pre[i]
        pre[i] = curr
        
    return max(pre)
    
limit = int(1e5)
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def write(index, reservation):
    assert len(reservation) <= limit
    with open(f"input/input{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{reservation}\n")
        print(index, len(reservation))

    result = hotelReservations(reservation)
    with open(f"output/output{str(index).zfill(2)}.txt", "w") as f:
        f.write(f"{result}\n")

for index in range(10):
    lim = limit // 13
    if index < 5:
        lim = 100
    length = random.randint(1, lim)
    arr = numpy.random.randint(1, limit, size=(length,2)).tolist()
    reservation = '|'.join([f"{min(a, b)},{max(a, b)}" for a,b in arr])
    write(index, reservation)
    

index = 10
reservation = "1,3|2,4|3,5"
write(index, reservation)

index = 11
reservation = "1,1|2,2|1000,1000"
write(index, reservation)

index = 12
arr = numpy.random.randint(1, limit, size=(limit//13,2)).tolist()
reservation = '|'.join([f"{min(a, b)},{max(a, b)}" for a,b in arr])
write(index, reservation)

index = 13
arr = [[random.randint(1, limit)] * 2 for i in range(1,limit//13 + 1)]
reservation = '|'.join([f"{a},{b}" for a,b in arr])
write(index, reservation)

index = 14
arr = [[1, limit] for i in range(1,limit//13 + 1)]
reservation = '|'.join([f"{min(a, b)},{max(a, b)}" for a,b in arr])
write(index, reservation)

index = 15
arr = [[i * 3, i * 3 + 2] for i in range(1,limit//13 + 1)]
reservation = '|'.join([f"{min(a, b)},{max(a, b)}" for a,b in arr])
write(index, reservation)